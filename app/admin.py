# Copyright (c) 2009 Katie Parlante

from madtwitter.app.models import Stanza
from django.contrib import admin

class StanzaAdmin(admin.ModelAdmin):
    fields = [
        'search1', 'tweet1', 'user1', 'tweet_id1',
        'search2', 'tweet2', 'user2', 'tweet_id2',
        'search3', 'tweet3', 'user3', 'tweet_id3', 'count'
    ]
    
    list_display = ('search1', 'tweet1', 'search2', 'tweet2', 'search3', 'tweet3')
    search_fields = ['user1', 'user2', 'user3', 'tweet1', 'tweet2', 'tweet3']
    list_filter = ('created',)
    
admin.site.register(Stanza, StanzaAdmin)