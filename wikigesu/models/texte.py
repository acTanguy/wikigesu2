from django.db import models
from wikigesu.helpers.slugify import unique_slugify
from wikigesu.helpers.slugify import unique_itemify
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed


class Texte(models.Model):
    class Meta:
        app_label="wikigesu"

    titre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    item = models.SlugField(blank=True, null=True)
    titre_traduit = models.CharField(max_length=255, blank=True, null=True)
    auteur = models.ForeignKey('wikigesu.Personne', related_name='ecrit_par', blank=True, null=True)
    recueil_litteraire = models.CharField(max_length=255, blank=True, null=True)
    forme_litteraire = models.CharField(max_length=255, blank=True, null=True)
    rimes = models.CharField(max_length=255, blank=True, null=True)
    corps_texte = models.TextField(blank=True, null=True)

    remarques = models.TextField(blank=True, null=True)

    source = models.URLField(max_length=200,blank=True, null=True)

    def save(self, **kwargs):
    	slug_str = "%s" % (self.titre) 
    	unique_slugify(self, slug_str) 
    	item_str = "%s" % (self.rimes)
	unique_itemify(self, item_str)
	super(Texte, self).save()

    def __unicode__(self):
        return u"{0}".format(self.titre)

@receiver(post_save, sender=Texte)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:wikigesu_texte item_id:{0}".format(instance.id), q_op="AND")
    if record:
        solrconn.delete(record.results[0]['id'])

    texte = instance
    d = {
        'type':'wikigesu_texte',
        'id':str(uuid.uuid4()),
        'titre':texte.titre,
        'auteur':texte.auteur,
	'slug':texte.slug,        

    }
    solrconn.add(**d)
    solrconn.commit()
