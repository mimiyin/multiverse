import sys
import os

from django.core.management.base import BaseCommand, CommandError

import requests
from PIL import Image, ImageFont, ImageDraw

import tweepy

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
width = 880
height = 440
scale = .5
margin = 40*scale
ratio = .95
lg = ImageFont.truetype(PROJECT_PATH + '/static/fonts/times.ttf', 96)
med = ImageFont.truetype(PROJECT_PATH + '/static/fonts/times.ttf', 36)
sm = ImageFont.truetype(PROJECT_PATH + '/static/fonts/times.ttf', 24)

def shake_hands():
    consumer_key = 'uKC3vb6nLTrwFQN4A1MM6yXtr'
    consumer_secret = 'r99uNe9JPeThrV2Iyqq7fyEaHP9BKJ5eU1EAqmy5raQX37R33k'
    
    access_token="755697409-YxhFvvk3ETcGsoV9daOOEHrdkDM9473zTXZ7tEWt"
    access_token_secret="zjeRi7dqZGypYdAzCqpf4qY73Pb5a7zjFMKU5kuwrAqiG"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
            
    return tweepy.API(auth) 

twitter = shake_hands()

def resize(font, txt, sz):
    while(font.getsize(txt)[0] > ratio*width):
        sz-=1
        font = ImageFont.truetype(PROJECT_PATH + '/static/fonts/times.ttf', sz)
    return font

import time
import random               
def process(sets):
    # make images for each poem
    count = 0
    poems = []
    timers = []
    for set in sets:
        poems.extend(set)
    total = len(poems)
    interval = int((24*60*60)/total)
    random.shuffle(poems)
    for p,poem in enumerate(poems):
        pm = { 'tweeters' : [], 'lines' : [] }
        img = Image.new('RGB', (width, height))
        draw=ImageDraw.Draw(img)
        
        lines = []
        for l, line in enumerate(poem):
            line = line[0] + " " + line[1]  
            lines.append((line, lg.getsize(line)))                        
        max_line = max(lines, key=lambda item:item[1])[0]
        font = resize(lg, max_line, 96)
        
        lh = margin
        for l, line in enumerate(poem):
            pm['tweeters'].append('@' + line[2])
            ln = line[0] + " " + line[1]
            draw.text((margin,lh), ln, fill=(256,256,256), font=font)
            this_lh = font.getsize(ln)[1]
            lh += this_lh + margin
            
        tweeters = (' ').join(pm['tweeters'])
        draw.text((margin,lh), tweeters, fill=(128,128,128), font=med)
        wm = 'http://multivers.es'
        wm_size = sm.getsize(wm)
        draw.text((width-wm_size[0]-margin,height-wm_size[1]-margin), wm, fill=(128,128,128), font=sm)
        img.resize((int(width*scale),int(height*scale)), resample=Image.ANTIALIAS)
        img_file = PROJECT_PATH + '/static/images/tweet.png'
        img.save(img_file, 'PNG')
        twitter.update_with_media(img_file, 'http://multivers.es by ' + tweeters)
        time.sleep(1800)

class Command(BaseCommand):
    
        def handle(self, *args, **options):  
            sets = []
            # make a request
            titles = ['transit', 'contemplation', 'aspiration']
            for t,title in enumerate(titles):
                r = requests.get('http://multivers.es/' + title + '.html', params={ 'load' : 1, 'json' : 1, 'page' : 0 })
                set = r.json()
                sets.append(set)
                print str(t) + ': ' + str(len(set))
                if(len(sets) == 3):
                    process(sets)