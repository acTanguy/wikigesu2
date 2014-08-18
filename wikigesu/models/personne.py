
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Personne(models.Model):
    class Meta:
        app_label="wikigesu"

    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    variante_nom = models.CharField(max_length=255, blank=True, null=True)
    nom_bref = models.CharField(max_length=255, blank=True, null=True)
    date_naissance = models.CharField(max_length=16, blank=True, null=True)
    lieu_naissance = models.ForeignKey("wikigesu.Localisation", related_name='lieu_de_naissance_de', blank=True, null=True)
    date_mort = models.CharField(max_length=16, blank=True, null=True)
    lieu_mort  = models.ForeignKey("wikigesu.Localisation", related_name='lieu_de_mort_de', blank=True, null=True)
    role = models.ManyToManyField("wikigesu.Role", blank=True, null=True, related_name='activite_de')
    lieu_activite = models.ManyToManyField("wikigesu.Localisation", related_name='lieu_d_activite_de', blank=True, null=True)
    periode_activite = models.CharField(max_length=16, blank=True, null=True)

    bibliographie = models.TextField(blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.nom, self.prenom)

    def nom_complet(self):
	return u"{0}, {1}".format(self.nom, self.prenom)
