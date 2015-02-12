from django.conf.urls import patterns, include, url
from django.contrib import admin
from spellcorrection.views import SuggestionList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marketiq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^suggestions/$', SuggestionList.as_view()),
)
