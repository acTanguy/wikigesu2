from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from wikigesu.helpers.slugify import unique_itemify

class Piece(models.Model):
    class Meta:
        app_label="wikigesu"

    item = models.SlugField(db_index=True, blank=True, unique=True, null=True)
    titre = models.CharField(max_length=255)
    recueil_id = models.ForeignKey("wikigesu.Recueil", to_field='recueil_id', related_name='pieces_de', blank=True, null=True)
    place_dans_recueil = models.IntegerField(max_length=4, blank=True, null=True)
    compositeur = models.ForeignKey('wikigesu.Personne', related_name='piece compose par', blank=True, null=True)
    poete =  models.ForeignKey('wikigesu.Personne',related_name='ecrit par', blank=True, null=True)
    texte = models.ForeignKey('wikigesu.Texte', related_name='texte_litteraire', blank=True, null=True)
    concordance_ms = models.ManyToManyField("self", blank=True, null=True)
    concordance_imp = models.ManyToManyField("self", blank=True, null=True)
    nombre_de_voix = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ForeignKey('wikigesu.GenreMusicalNormalise', blank=True, null=True)
    genre_musical_detaille = models.ForeignKey('wikigesu.GenreMusicalDetaille', blank=True, null=True)
    pdf_link = models.URLField(max_length=200,blank=True, null=True)
    mei_link = models.URLField(max_length=200,blank=True, null=True)
    mp3_link = models.URLField(max_length=200,blank=True, null=True)
    fichiers_joints = models.ManyToManyField('wikigesu.File', blank=True, null=True)

    remarques = models.TextField(blank=True, null=True)

    def save(self, **kwargs):
        item_str = "%s/%s" % (self.recueil_id.recueil_id, self.place_dans_recueil)
        unique_itemify(self, item_str)
        super(Piece, self).save()


    def __unicode__(self):
        return u"{0}".format(self.titre)

    

@receiver(post_save, sender=Piece)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:wikigesu_piece item:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    piece = instance
    d = {
        'type':'wikigesu_piece',
        'id':str(uuid.uuid4()),
        'titre':piece.titre,
        'recueil_id':piece.recueil_id,
	'item':piece.item,
        
    }
    solrconn.add(**d)
    solrconn.commit()

