import os
from django.conf.urls.defaults import *
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Example:
    # (r'^madtwitter/', include('madtwitter.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    
    (r'^$', 'madtwitter.app.views.street'),
    
    (r'^14thstreet/$', 'madtwitter.app.views.street'),
    (r'^14thstreet/(?P<title>transit)/$', 'madtwitter.app.views.street'),
    (r'^14thstreet/(?P<title>contemplation)/$', 'madtwitter.app.views.street'),
    (r'^14thstreet/(?P<title>aspiration)/$', 'madtwitter.app.views.street'),
    (r'^14thstreet/(?P<title>office)/$', 'madtwitter.app.views.street'),
    
    (r'^(?P<title>transit)/$', 'madtwitter.app.views.street'),
    (r'^(?P<title>contemplation)/$', 'madtwitter.app.views.street'),
    (r'^(?P<title>aspiration)/$', 'madtwitter.app.views.street'),
    (r'^(?P<title>explore)/$', 'madtwitter.app.views.street'),

    (r'^14thstreet/add/$', 'madtwitter.app.views.add_best'),
    (r'^add/$', 'madtwitter.app.views.add_best'),
    (r'^best/$', 'madtwitter.app.views.show_best'),
    (r'^about/$', 'madtwitter.app.views.about'),
    (r'^press/$', 'madtwitter.app.views.chance'),    
    (r'^chance/$', 'madtwitter.app.views.chance'),    
    (r'^share/$', 'madtwitter.app.views.recent'),
    
    (r'^37thstreet/$', 'madtwitter.app.views.window'),
    (r'^37thstreet/(?P<title>transit)/$', 'madtwitter.app.views.window'),
    (r'^37thstreet/(?P<title>aspiration)/$', 'madtwitter.app.views.window'),
    (r'^37thstreet/(?P<title>office)/$', 'madtwitter.app.views.window'),
    
    (r'^projection/$', 'madtwitter.app.views.projection'),
    (r'^projection/(?P<title>transit)/$', 'madtwitter.app.views.projection'),
    (r'^projection/(?P<title>contemplation)/$', 'madtwitter.app.views.projection'),
    (r'^projection/(?P<title>aspiration)/$', 'madtwitter.app.views.projection'),
    (r'^projection/(?P<title>office)/$', 'madtwitter.app.views.projection'),
    
    (r'^transit\.html$', 'madtwitter.app.views.transit'),
    (r'^contemplation\.html$', 'madtwitter.app.views.contemplation'),
    (r'^aspiration\.html$', 'madtwitter.app.views.aspiration'),
    (r'^office\.html$', 'madtwitter.app.views.office'),
    (r'^explore\.html$', 'madtwitter.app.views.explore'),
    
    (r'^dumbo/$', 'madtwitter.app.views.dumbo'),
    (r'^political\.html$', 'madtwitter.app.views.political_statements'),
    
    #(r'^relationship/$', 'madtwitter.app.views.relationship_cycle'),
    (r'^relationship\.html$', 'madtwitter.app.views.relationship_statements'),
    
    #(r'^comparison/$', 'madtwitter.app.views.comparison_cycle'),
    (r'^comparison\.html$', 'madtwitter.app.views.comparison_statements'),
    
    (r'^lab/$', 'madtwitter.app.views.search_lab'),
    (r'^cycle/$', 'madtwitter.app.views.cycle_custom'),
    (r'^animation/$', 'madtwitter.app.views.animation_lab'),
    
    (r'^tweets/$', 'madtwitter.app.views.tweets'),
    (r'^phrases/$', 'madtwitter.app.views.phrases'),
    (r'^lines/$', 'madtwitter.app.views.three_lines'),
    
     (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),   
    
#    (r'^js/(.*)', serve,   
#        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),
#    (r'^css/(.*)', serve,   
#        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),    
)

