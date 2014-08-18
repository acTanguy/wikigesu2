from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from wikigesu.helpers.slugify import unique_itemify

class Recueil(models.Model):
    class Meta:
        app_label = "wikigesu"


    IMPRIME = 'imprime'
    MANUSCRIT = 'manuscrit'
    CHOIX_FORMAT = (
        (MANUSCRIT, 'manuscrit'),
        (IMPRIME, 'imprime'),
    )

    recueil_item = models.SlugField(db_index=True, blank=True, unique=True, null=True)
    recueil_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    titre_complet = models.CharField(max_length=255, blank=True, null=True)
    titre_complet_traduit_FR = models.CharField(max_length=255, blank=True, null=True)
    titre_complet_traduit_EN = models.CharField(max_length=255, blank=True, null=True)
    titre_court = models.CharField(max_length=255, blank=True, null=True)
    titre_court_traduit_FR = models.CharField(max_length=255, blank=True, null=True)
    titre_court_traduit_EN = models.CharField(max_length=255, blank=True, null=True)

    catalogue_id = models.ManyToManyField('wikigesu.Catalogue', blank=True, null=True)
    support = models.CharField(max_length=9, choices=CHOIX_FORMAT, default=IMPRIME)
    ville_edition = models.ForeignKey('wikigesu.Localisation', blank=True, null=True)
    datation = models.CharField(max_length=255, blank=True, null=True)

    editeur = models.ManyToManyField('wikigesu.Personne', related_name='edite_par', blank=True, null=True)
    libraire = models.ManyToManyField('wikigesu.Personne', related_name='imprime_par', blank=True, null=True)
    copiste = models.ManyToManyField('wikigesu.Personne', related_name='copie_par', blank=True, null=True)
    compositeurs = models.ManyToManyField('wikigesu.Personne', related_name='compose_par', blank=True, null=True)

    nombre_pieces = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField('wikigesu.GenreMusicalNormalise', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField('wikigesu.GenreMusicalDetaille', blank=True, null=True)
    reedition = models.ManyToManyField("self", blank=True, null=True)
    
    remarques = models.TextField(blank=True, null=True)

    def save(self, **kwargs):
	item_str = "%s" % (self.recueil_id)
        unique_itemify(self, item_str)
	super(Recueil, self).save()

    def __unicode__(self):
        return u"{0}, {1}".format(self.titre, self.datation)

@receiver(post_save, sender=Recueil)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr
    from wikigesu.models.personne import Personne

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:wikigesu_recueil item:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    recueil = instance
    nom_compositeurs = []
    for f in recueil.compositeurs.all():
        nom = "{0}, {1}".format(f.nom, f.prenom)
        nom_compositeurs.append(nom)
    d = {
        'type':'wikigesu_recueil',
        'id':str(uuid.uuid4()),
        'item':recueil.recueil_item,
        'recueil_id':recueil.recueil_id,
        'titre_complet':recueil.titre_complet,
        'titre_complet_traduit_EN':recueil.titre_complet_traduit_EN,
        'titre_court':recueil.titre_court,
        'titre_court_traduit_EN':recueil.titre_court_traduit_EN,
        'titre_traduit':recueil.titre_traduit,
        'nom_compositeurs':nom_compositeurs,
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Recueil)
def solr_delete(sender, instance, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:wikigesu_recueil item:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])
