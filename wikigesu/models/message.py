from django.db import models
from wikigesu.models.piece import Piece
from wikigesu.models.utilisateur import UtilisateurProfile
import os

def new_path(path):
	def wrapper(instance, filename):
		extension = filename.split(',')[-1]
		filename = '{}.{}'.format(instance.pk, extension)
		return path.os.join(path, filename)
	return wrapper

class Message(models.Model):
	posteur = models.ForeignKey(UtilisateurProfile, null=True, blank=True)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	piece = models.ForeignKey(Piece)
	voix = models.CharField(max_length=10)
	mesure = models.SmallIntegerField()
	validee = models.BooleanField(default=False)
	archive = models.BooleanField(default=False)
	ip = models.GenericIPAddressField()
	#mail = models.EmailField(max_length=254)
	fichier = models.FileField(null=True, upload_to=os.path.join("fichiers_utilisateur"))
	class Meta:
		app_label="wikigesu"
		permissions = (
			('valider_message', 'Peut valider les messages'),
			('archiver_message', 'Peut archiver les messages'),
		)
	def __unicode__(self):
		if self.posteur == None:
			return "Internaute {0}...".format(self.message[:25])
		else:
			return "{0} {1}...".format(self.posteur.personne.nom_bref, self.message[:25])
