import os
from django.conf.urls import *
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Example:
    # (r'^madtwitter/', include('multiverse.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    
    (r'^$', 'multiverse.app.views.street'),
    
    (r'^14thstreet/$', 'multiverse.app.views.street'),
    (r'^14thstreet/(?P<title>transit)/$', 'multiverse.app.views.street'),
    (r'^14thstreet/(?P<title>contemplation)/$', 'multiverse.app.views.street'),
    (r'^14thstreet/(?P<title>aspiration)/$', 'multiverse.app.views.street'),
    (r'^14thstreet/(?P<title>office)/$', 'multiverse.app.views.street'),
    
    (r'^(?P<title>transit)/$', 'multiverse.app.views.street'),
    (r'^(?P<title>contemplation)/$', 'multiverse.app.views.street'),
    (r'^(?P<title>aspiration)/$', 'multiverse.app.views.street'),
    (r'^(?P<title>explore)/$', 'multiverse.app.views.street'),
    (r'^(?P<title>selections)/$', 'multiverse.app.views.street'),

    (r'^14thstreet/add/$', 'multiverse.app.views.add_best'),
    (r'^add/$', 'multiverse.app.views.add_best'),
    (r'^best/$', 'multiverse.app.views.show_best'),
    (r'^about/$', 'multiverse.app.views.about'),
    (r'^press/$', 'multiverse.app.views.chance'),    
    (r'^chance/$', 'multiverse.app.views.chance'),    
    (r'^share/$', 'multiverse.app.views.recent'),
    
    (r'^37thstreet/$', 'multiverse.app.views.window'),
    (r'^37thstreet/(?P<title>transit)/$', 'multiverse.app.views.window'),
    (r'^37thstreet/(?P<title>aspiration)/$', 'multiverse.app.views.window'),
    (r'^37thstreet/(?P<title>office)/$', 'multiverse.app.views.window'),
    
    (r'^projection/$', 'multiverse.app.views.projection'),
    (r'^projection/(?P<title>transit)/$', 'multiverse.app.views.projection'),
    (r'^projection/(?P<title>contemplation)/$', 'multiverse.app.views.projection'),
    (r'^projection/(?P<title>aspiration)/$', 'multiverse.app.views.projection'),
    (r'^projection/(?P<title>office)/$', 'multiverse.app.views.projection'),

    (r'^select\.html$', 'multiverse.app.views.select'),    
    (r'^transit\.html$', 'multiverse.app.views.transit'),
    (r'^contemplation\.html$', 'multiverse.app.views.contemplation'),
    (r'^aspiration\.html$', 'multiverse.app.views.aspiration'),
    (r'^office\.html$', 'multiverse.app.views.office'),
    (r'^explore\.html$', 'multiverse.app.views.explore'),
    
    (r'^dumbo/$', 'multiverse.app.views.dumbo'),
    (r'^political\.html$', 'multiverse.app.views.political_statements'),
    
    #(r'^relationship/$', 'multiverse.app.views.relationship_cycle'),
    (r'^relationship\.html$', 'multiverse.app.views.relationship_statements'),
    
    #(r'^comparison/$', 'multiverse.app.views.comparison_cycle'),
    (r'^comparison\.html$', 'multiverse.app.views.comparison_statements'),
    
    (r'^lab/$', 'multiverse.app.views.search_lab'),
    (r'^cycle/$', 'multiverse.app.views.cycle_custom'),
    (r'^animation/$', 'multiverse.app.views.animation_lab'),
    
    (r'^tweets/$', 'multiverse.app.views.tweets'),
    (r'^phrases/$', 'multiverse.app.views.phrases'),
    (r'^lines/$', 'multiverse.app.views.three_lines'),
    
    (r'^robots\.txt$',  TemplateView.as_view( template_name ='robots.txt')),   
        
    (r'^js/(.*)', serve,   
        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),
    (r'^css/(.*)', serve,   
        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),    
    #urls for emoji
    (r'^emoji/', include('emoji.urls')),
)

