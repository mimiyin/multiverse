import os
from django.conf.urls import *
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    
    (r'^$', 'myproject.app.views.street'),
    
    (r'^14thstreet/$', 'myproject.app.views.street'),
    (r'^14thstreet/(?P<title>transit)/$', 'myproject.app.views.street'),
    (r'^14thstreet/(?P<title>contemplation)/$', 'myproject.app.views.street'),
    (r'^14thstreet/(?P<title>aspiration)/$', 'myproject.app.views.street'),
    (r'^14thstreet/(?P<title>office)/$', 'myproject.app.views.street'),
    
    (r'^(?P<title>transit)/$', 'myproject.app.views.street'),
    (r'^(?P<title>contemplation)/$', 'myproject.app.views.street'),
    (r'^(?P<title>aspiration)/$', 'myproject.app.views.street'),
    (r'^(?P<title>explore)/$', 'myproject.app.views.street'),

    (r'^14thstreet/add/$', 'myproject.app.views.add_best'),
    (r'^add/$', 'myproject.app.views.add_best'),
    (r'^best/$', 'myproject.app.views.show_best'),
    (r'^about/$', 'myproject.app.views.about'),
    (r'^press/$', 'myproject.app.views.chance'),    
    (r'^chance/$', 'myproject.app.views.chance'),    
    (r'^share/$', 'myproject.app.views.recent'),
    
    (r'^37thstreet/$', 'myproject.app.views.window'),
    (r'^37thstreet/(?P<title>transit)/$', 'myproject.app.views.window'),
    (r'^37thstreet/(?P<title>aspiration)/$', 'myproject.app.views.window'),
    (r'^37thstreet/(?P<title>office)/$', 'myproject.app.views.window'),
    
    (r'^projection/$', 'myproject.app.views.projection'),
    (r'^projection/(?P<title>transit)/$', 'myproject.app.views.projection'),
    (r'^projection/(?P<title>contemplation)/$', 'myproject.app.views.projection'),
    (r'^projection/(?P<title>aspiration)/$', 'myproject.app.views.projection'),
    (r'^projection/(?P<title>office)/$', 'myproject.app.views.projection'),
    
    (r'^transit\.html$', 'myproject.app.views.transit'),
    (r'^contemplation\.html$', 'myproject.app.views.contemplation'),
    (r'^aspiration\.html$', 'myproject.app.views.aspiration'),
    (r'^office\.html$', 'myproject.app.views.office'),
    (r'^explore\.html$', 'myproject.app.views.explore'),
    
    (r'^dumbo/$', 'myproject.app.views.dumbo'),
    (r'^political\.html$', 'myproject.app.views.political_statements'),
    
    #(r'^relationship/$', 'myproject.app.views.relationship_cycle'),
    (r'^relationship\.html$', 'myproject.app.views.relationship_statements'),
    
    #(r'^comparison/$', 'myproject.app.views.comparison_cycle'),
    (r'^comparison\.html$', 'myproject.app.views.comparison_statements'),
    
    (r'^lab/$', 'myproject.app.views.search_lab'),
    (r'^cycle/$', 'myproject.app.views.cycle_custom'),
    (r'^animation/$', 'myproject.app.views.animation_lab'),
    
    (r'^tweets/$', 'myproject.app.views.tweets'),
    (r'^phrases/$', 'myproject.app.views.phrases'),
    (r'^lines/$', 'myproject.app.views.three_lines'),
    
     (r'^robots\.txt$',  TemplateView.as_view( template_name ='robots.txt'), 'robots'),   
    
    (r'^js/(.*)', serve,   
        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),
    (r'^css/(.*)', serve,   
        {'document_root': os.path.join(os.path.dirname(__file__), "static")}),    
)

