from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from wikigesu.views.search import SearchView
from wikigesu.views.auth import LogoutView
from wikigesu.views.auth import LoginFormView

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'wikigesu.views.main.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^recueils/$', 'wikigesu.views.main.recueils', name='recueils'),
    url(r'^pieces/$', 'wikigesu.views.main.pieces', name='pieces'),
    url(r'^edition/(?P<pk>\w+)$', 'wikigesu.views.main.recueil', name='recueil'),
    url(r'^edition/(?P<recueil>\w+)/(?P<place>\d+)$', 'wikigesu.views.main.piece', name='piece'),
    url(r'^textes/$', 'wikigesu.views.main.textes', name='textes'),
    url(r'^texte/(?P<pk>[\w\-]+)$', 'wikigesu.views.main.texte', name='texte'),
    url(r'^$', 'wikigesu.views.main.home', name='accueil'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^equipe/$', 'wikigesu.views.main.equipe', name='equipe'), 
    url(r'^traitements/', include('wikigesu.urlsTraitements', namespace='traitements')),
    url(r'^login/', LoginFormView.as_view(), name="login-view"),
    url(r'^logout/', LogoutView.as_view(), name="logout-view"),
    url(r'^search/$', SearchView.as_view(), name="search-view"),
)

if settings.DEBUG:
	urlpatterns += patterns('', url(r'^wikigesu/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}), url(r'^wikigesu/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,})) 
