from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^addCom$', 'wikigesu.views.traitements.ajoutCommentaire', name='ajoutCommentaire'),
	url(r'^remCom$', 'wikigesu.views.traitements.refuseCommentaire', name='supprimerCommentaire'),
	url(r'^validateCom$', 'wikigesu.views.traitements.valideCommentaire', name='valideCommentaire'),
	url(r'^archiveCom', 'wikigesu.views.traitements.archiveCommentaire', name='archiveCommentaire'),
)
