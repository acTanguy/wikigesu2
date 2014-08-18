from django.db import models



class Exemplaire(models.Model):
    class Meta:
        app_label="wikigesu"

    CONSERVE = "CONSERVE"
    MANQUANT = "MANQUANT"
    COMPLET = 'COMPLET'
    INCOMPLET = 'INCOMPLET'
    CHOIX_ETAT =(
        (COMPLET, 'Complet'),
        (INCOMPLET, 'Incomplet'),
    )
    CHOIX_CONSERVATION = (
        (CONSERVE, 'Conserve'),
        (MANQUANT, 'Manquant'),
    )

    localisation = models.ForeignKey('wikigesu.Bibliotheque', blank=True, null=True)
    recueil_id = models.ForeignKey("wikigesu.Recueil", to_field='recueil_id', related_name='localise', blank=True, null=True)
    cote_exemplaire = models.CharField(max_length=16, blank=True, null=True)
    etat = models.CharField(max_length=9, choices=CHOIX_ETAT, default=COMPLET)
    conserve_manquant = models.CharField(max_length=9, choices=CHOIX_CONSERVATION, default=COMPLET)
    remarques_exemplaires = models.TextField(blank=True, null=True)
    lien_source = models.URLField(max_length=200,blank=True, null=True)

    nom_voix =models.CharField(max_length=16, blank=True, null=True)
    composant_conserve = models.CharField(max_length=255, blank=True, null=True)
    composant_manquant =models.CharField(max_length=255, blank=True, null=True)

    remarques_voix =models.TextField(blank=True, null=True)



    def __unicode__(self):
        return u"{0}".format(self.cote_exemplaire)

