from django.conf.urls import patterns, include, url
from django.contrib import admin
from spellcorrection.views import HomeView, SuggestView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'marketiq.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', HomeView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^suggest/$', SuggestView.as_view()),
                       )
