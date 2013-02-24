# Copyright (c) 2009 Katie Parlante

from django.db import models

class Stanza(models.Model):
    
    user1 = models.CharField(max_length=20)
    user2 = models.CharField(max_length=20)
    user3 = models.CharField(max_length=20)
    
    search1 = models.CharField(max_length=150)
    search2 = models.CharField(max_length=150)
    search3 = models.CharField(max_length=150)
    
    tweet1 = models.CharField(max_length=150)
    tweet2 = models.CharField(max_length=150)
    tweet3 = models.CharField(max_length=150)
    
    tweet_id1 = models.CharField(max_length=50)
    tweet_id2 = models.CharField(max_length=50)
    tweet_id3 = models.CharField(max_length=50)
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    count = models.IntegerField(default=1)
    
    class Meta:
        unique_together = ("user1", "user2", "user3", "tweet_id1", "tweet_id2", "tweet_id3")
    
