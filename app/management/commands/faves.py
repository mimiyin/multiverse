from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time

from django.core.management.base import BaseCommand, CommandError

import tweepy

def shake_hands():
    consumer_key = 'uKC3vb6nLTrwFQN4A1MM6yXtr'
    consumer_secret = 'r99uNe9JPeThrV2Iyqq7fyEaHP9BKJ5eU1EAqmy5raQX37R33k'
    
    access_token="755697409-YxhFvvk3ETcGsoV9daOOEHrdkDM9473zTXZ7tEWt"
    access_token_secret="zjeRi7dqZGypYdAzCqpf4qY73Pb5a7zjFMKU5kuwrAqiG"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
            
    return tweepy.API(auth) 

class Command(BaseCommand):    
    def handle(self, *args, **options):
        twitter = shake_hands()
        # get cached faves
        faves = cache.get('faves')
        if not faves:
            # get last time we checked for faves
            since = cache.get('since')
            print 'Get since: %s' % since
            if since is None:
                since = time.time()
                cache.set('since', since, 24*60*60)
                print 'Set since to: %s' % since
                return
            faves = twitter.favorites('multivers_es', since_id = since) 
        print 'Length of faves %s' % len(faves)
        # save the faves
        fave = faves.pop()
        tweeters = ''
        for user in fave.entities['user_mentions']:
            tweeters += ' @' + user['screen_name']
        img_file = fave.entities['media'][0]['media_url']
        print '%s: %s' %(tweeters, img_file)
        #twitter.update_with_media(img_file, 'Select http://multivers.es by ' + tweeters + ' #tweetpoem #poem')
        cache.set('faves', faves, 24*60*60)
        cache.set('since', time.time(), 24*60*60)
        print 'Length of faves %s' % len(faves)
