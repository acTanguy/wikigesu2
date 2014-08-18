from django.db import models

class Localisation(models.Model):
    class Meta:
        app_label="wikigesu"

    pays_normalise = models.CharField(max_length=255)
    pays_francais = models.CharField(max_length=255n null=True)
    pays_anglais = models.CharField(max_length=255n null=True)
    nom_ville_normalise = models.CharField(max_length=255, blank=True, null=True, unique=True)
    nom_ville_francais = models.CharField(max_length=255, blank=True, null=True, unique=True)
    nom_ville_anglais = models.CharField(max_length=255, blank=True, null=True, unique=True)
    nom_ville_source = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.pays_normalise_langue, self.nom_ville_normalise_langue)

    @property
    def nom_lieu(self):
	if self.nom_ville_normalise_langue:
	    return u"{0}, ({1})".format(self.nom_ville_normalise_langue, self.pays_normalise_langue)
	else:
	    return u"{0}".format(self.pays_normalise_langue)
