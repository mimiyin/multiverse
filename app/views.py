# Copyright (c) 2009 Katie Parlante

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.db import IntegrityError

import urllib
import simplejson
import re
import random

import base64
import httplib

import tweepy
from multiverse.app.models import Stanza

def shake_hands(phrase):

    consumer_key = 'UcAG75lm90EeO6F5VLGbPQ'
    consumer_secret = 'UqZxtmpfq0qa2mybVL4GiJzIknroE9U4vrrmvJD0w'
    
    access_token="755697409-VuI4qRuBpI3mjGDLNagocq1YH6oZ3I5yhon7PWTp"
    access_token_secret="3bnfPCNO8BoYKHHthEni2heYumSRrraxgwA8l05Wg"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)    
    return api.search(q=phrase, rpp=100)



def screen(alist):
    exp = re.compile(r'twitter|tweet|http|facebook|nigger|nigga|cunt|@|#|followers|rt|<3|lol', re.IGNORECASE)
    return [(text,user,tweet_id) for (text,user,tweet_id) in alist if not exp.search(text)]
    
def decode(txt):
    return txt.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
    
def phrase_list(phrase, clean_list):
    exp = re.compile(phrase + r' ([^,.!?:;()=~-]+)', re.IGNORECASE)
    return [(m.group(1),user,tweet_id) for (m,user,tweet_id) in [(exp.search(item),user,tweet_id) for (item,user,tweet_id) in clean_list] if m]
    
def short_filter(phrase_list):
    return [p for p in phrase_list if len(p[1]) < 35]

def fetch(phrase, page=1):
    phraselet = '"' + phrase + '"' + '+exclude:retweets'
    all_results=shake_hands(phraselet)   
    
    results = []
    for result in all_results:
        results.append({'text' : result.text, 'from_user': result.user.screen_name, 'id' : result.id})
        

    # Do the screening *after* we've picked the phrase out of the tweet -- in case the offending word was not in our selection
    return phrase_list(phrase, screen([(decode(entry['text']), entry['from_user'], entry['id']) for entry in results])) 
    #print screen(phrase_list(phrase, [(decode(entry['text']), entry['from_user'], entry['id']) for entry in results]))
    
    
    # diagnostics
    #total_list = screen(phrase_list(phrase, [(decode(entry['text']), entry['from_user'], entry['id']) for entry in results]))
    #print url, " ", len(total_list), len([p for p in total_list if len(p[0]) < 35])
    #return total_list
    
def tweets(request):
    template_file = "tweets.html"
    
    waiting_for_list = fetch("waiting for")
    thinking_about_list = fetch("thinking about")
    looking_at_list = fetch("looking at")
    wondering_why_list = fetch("wondering why")
    hoping_for_list = fetch("hoping for")
    
    tweets = zip(waiting_for_list, 
                 looking_at_list, 
                 thinking_about_list, 
                 wondering_why_list,
                 hoping_for_list)
    
    print tweets                              
    
    tweets.reverse()
    
    template_values = {
        "tweets" : tweets
    }
    
    #random_stanzas(request)
    
    return render_to_response(template_file, template_values)

def load_stanza(stanza_searches):
    search_results = []
    
    for search_group in stanza_searches:
        group_list = []
        for search_phrase in search_group: 
            phrase_list = [(search_phrase, phrase, user, tweet_id) for (phrase, user, tweet_id) in fetch(search_phrase)]
            
            if len(search_group) < 5:
                phrase_list += [(search_phrase, phrase, user, tweet_id) for (phrase, user, tweet_id) in fetch(search_phrase, 2)]
            group_list += short_filter(phrase_list)
        random.shuffle(group_list)
        # diagnostics
        #print group_list[0], len(group_list)
        search_results.append(group_list)
        
    return zip(*search_results)

def transit(request):
    
    search_terms = [
        ["On my way", "Walking around", "Walking to", "Walking from", "Running towards", "Running to", "Running from", "Heading uptown", "Heading downtown"],
        ["wondering why", "wondering if", "hoping for", "looking for", "looking around", "wondering about", "yearning for", "longing for", "desperate for", "waiting for", "waiting around for", "feeling like"],
        ["just saw", "just overheard", "just noticed", "just ran into", "just remembered", "just bumped into", "stumbled upon", "barely noticed"]
    ]
    
    return random_stanzas(request, "transit", search_terms)
    
def contemplation(request):
    
    search_terms = [
        ["Savoring", "Enjoying", "Worrying about", "Wondering about", "Wondering if", "Wondering why", "Relishing", "Reveling in", "Angry about", "Delighting in", "Escaping to"],        
        ["eating", "drinking", "nibbling", "munching", "sipping"],
        ["reading", "thinking about", "wishing for", "contemplating", "trying to forget", "remembering", "forgetting", "reminiscing", "recollecting"]
    ]
    
    return random_stanzas(request, "contemplation", search_terms)
    
def aspiration(request):
    
    search_terms = [
        ["I wish", "I have to have", "I need", "I would like to be", "I long for", "I yearn for", "I hope", "I still", "I desire", "I want to be", "I used to want to be", "I used to be"],
        ["with", "without"],
        ["unless", "besides", "apart from", "short of", "except for", "except if", "until"]
    ]
    
    return random_stanzas(request, "aspiration", search_terms)
    
def office(request):
    
    search_terms = [
        ["Reviewing", "Meeting with", "Working on", "Organizing the", "Finishing the"],
        ["demanding that", "discussing", "arranging", "speaking with", "handing over"],
        ["bored by", "expecting", "regretting", "frustrated with", "avoiding", "waiting for", "looking forward to"]
    ]
    
    return random_stanzas(request, "office", search_terms)
    
def explore(request):
    
    search_terms = [
        ["Visiting the", "Visiting a", "Visiting my", "Exploring", "Experiencing", "Discovering", "Returning to", "Travelling through", "Returning home with"],
        ["arguing about", "laughing about", "enriched by"],
        ["pleased to see that", "disappointed to realize", "still dubious about", "bored by"]
    ]
    
    return random_stanzas(request, "explore", search_terms)
    
def random_stanzas(request, title, search_terms):
    print request.GET
    
    page = int(request.GET['page'])
    if 'size' in request.GET:
        page_size = int(request.GET['size'])
    else:
        page_size = 10
    force_cache_load = "load" in request.GET
    
    if force_cache_load:
        tweet_phrases = None
    else:
        request.session[title] = page + 1
        tweet_phrases = cache.get(title)
                
    if not tweet_phrases:
        tweet_phrases = load_stanza(search_terms)
        cache.set(title, tweet_phrases, 60*35)
        print "Loaded cache, size: %s" % len(tweet_phrases)
    
    page = page % (len(tweet_phrases)/page_size)    
    start = page*page_size
    end = (page+1)*page_size
    
    template_values = {
        "tweet_phrases" : tweet_phrases[start:end]
    }
    
    print "Calling random stanzas! len: %s page: %s start: %s end: %s" % (len(tweet_phrases), page, start, end)
        
    return render_to_response("random_tweets.html", template_values)
    
def political_statements(request):
    
    search_terms = [
        ["save the", "love the", "believe in"],
        ["down with", "to hell with", "stop the", "fuck the"]
    ]
    
    return random_stanzas(request, "political", search_terms)
    
def relationship_statements(request):
    
    search_terms = [
        ["my boss is", "my manager is", "my employee is", "my coworker is", 
        "my wife is", "my husband is", "my spouse is", "my partner is",
        "my brother is", "my sister is", "my son is", "my daughter is", "my child is",
        "my father is", "my mother is",
        "my friend is"]
    ]
    
    return random_stanzas(request, "relationship", search_terms)
    
def comparison_statements(request):
    
    search_terms = [
        ["similar to", "not unlike", "like a", "some call it", 
        "bigger than a", "smaller than a"]
    ]
    
def three_lines(request):
    template_file = "tweet_phrases.html"
    
    search_one = request.GET['one']
    search_two = request.GET['two']
    search_three = request.GET['three']
    
    page = request.GET['page']
    
    first_phrase = fetch(search_one, page)
    second_phrase = fetch(search_two, page)
    third_phrase = fetch(search_three, page)
    
    tweet_phrases = zip(first_phrase, second_phrase, third_phrase)
    
    tweet_phrases.reverse()
    
    template_values = {
        "tweet_phrases" : tweet_phrases,
        "search_one" : search_one,
        "search_two" : search_two,
        "search_three" : search_three
    }
    
    return render_to_response(template_file, template_values)

def phrases(request):    
    template_file = "phrases.html"
    
    search_phrase = request.GET['search_phrase']
    page = request.GET['page']
        
    tweet_list = fetch(search_phrase, page)
    
    template_values = {
        "tweet_list" : tweet_list,
        "search_phrase" : search_phrase
    }
    
    return render_to_response(template_file, template_values)

def main(request):
    template_file = "main.html"
        
    template_values = {
    }
    
    return render_to_response(template_file, template_values)
    
def cycle_custom(request):
    template_file = "cycle.html"

    search_one = request.GET['one']
    search_two = request.GET['two']
    search_three = request.GET['three']

    template_values = {
        "search_one" : search_one,
        "search_two" : search_two,
        "search_three" : search_three,
        "cycle" : "custom"
    }

    return render_to_response(template_file, template_values)
    
def cycle_random(request):
    
    template_values = {
        "cycle" : "random"
    }
    
    return render_to_response("cycle.html", template_values)

def street(request, title="transit"):
    
    template_values = {
        "cycle" : "random",
        "title" : title,
        "animation" : "fountain",
        "page" : request.session.get(title, 0)
    }
    
    return render_to_response("streetcycle.html", template_values, context_instance=RequestContext(request))
    
def projection(request, title="transit"):
    
    title_index = random.randint(0,2)
    
    if title_index == 0:
        title = "transit"
    elif title_index == 1:
        title = "aspiration"
    else:
        title = "contemplation"
    
    template_values = {
        "cycle" : "random",
        "title" : title,
        "animation" : "projectionAnimation",
        "page" : request.session.get(title, 0)
    }
    
    return render_to_response("projection.html", template_values)
    
def recent(request, title="transit"):
    
    template_values = {
        "cycle" : "none",
        "title" : title,
        "animation" : "none",
        "page" : request.session.get(title, 0)
    }
    
    return render_to_response("recent.html", template_values)
    
def window(request, title="office"):
    
    template_values = {
        "cycle" : "random",
        "title" : title,
        "animation" : "fountain",
        "page" : request.session.get(title, 0)
    }
    
    return render_to_response("window.html", template_values)

def dumbo(request):
    
    template_values = {
        "title" : "political",
        "animation" : "fadePair"
    }
    
    return render_to_response("dumbocycle.html", template_values)  

def add_best(request):
    
    s = Stanza()
    
    s.user1 = request.POST['user1']
    s.user2 = request.POST['user2']
    s.user3 = request.POST['user3']
    
    s.search1 = request.POST['search1']
    s.search2 = request.POST['search2']
    s.search3 = request.POST['search3']
    
    s.tweet1 = request.POST['tweet1']
    s.tweet2 = request.POST['tweet2']
    s.tweet3 = request.POST['tweet3']
    
    s.tweet_id1 = request.POST['tweet_id1']
    s.tweet_id2 = request.POST['tweet_id2']
    s.tweet_id3 = request.POST['tweet_id3']
    
    # IntegrityError is thrown if a duplicate entry is made,
    # so just pass in this case
    try:
        s.save()
    except IntegrityError:
        pass
    
    #return show_best(request);
    return HttpResponseRedirect(reverse('multiverse.app.views.show_best'))

def show_best(request):
        
    stanza_list = Stanza.objects.order_by('created')
    paginator = Paginator(stanza_list, 10)
    
    num_pages = paginator.num_pages
    page = int(request.GET.get('page', num_pages))
    
    stanzas = paginator.page(page)
    
    if (num_pages < 15):
        smart_range = paginator.page_range
    elif (page < 9):
        smart_range = range(1, 10)
        smart_range.append("...")
        smart_range.extend(range(num_pages-2, num_pages+1))
    elif (page > num_pages - 8):
        smart_range = range(1, 4)
        smart_range.append("...")
        smart_range.extend(range(num_pages-8, num_pages+1))
    else:
        smart_range = range(1, 4)
        smart_range.append("...")
        smart_range.extend(range(page-3, page+4))
        smart_range.append("...")
        smart_range.extend(range(num_pages-2, num_pages+1))
    
    template_values = {
        "stanzas" : stanzas,
        "page_num" : page,
        "smart_range" : smart_range
    }
    
    print template_values['stanzas']
    
    return render_to_response("best.html", template_values)

def about(request):
    template_values = {
    }
    return render_to_response("about.html", template_values)

def chance(request):
    template_values = {
    }
    return render_to_response("chance.html", template_values)

def animation_lab(request):
    template_file = "animation.html"

    template_values = {
    }

    return render_to_response(template_file, template_values)
    
def search_lab(request):
    template_file = "searches.html"

    template_values = {
    }

    return render_to_response(template_file, template_values)
