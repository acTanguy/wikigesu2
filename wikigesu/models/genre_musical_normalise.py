from django.db import models


class GenreMusicalNormalise(models.Model):
    class Meta:
        app_label="wikigesu"
        verbose_name = "Genre Musical Normalise"
        verbose_name_plural = "Genres Musicaux Normalises"

    PROFANE = 'profane'
    RELIGIEUX = 'religieux'

    CHOIX_STYLE = (
        (PROFANE, 'Profane'),
        (RELIGIEUX, 'Religieux'),
    )

    style = models.CharField(max_length=128, choices=CHOIX_STYLE, default=PROFANE)
    provenance = models.ForeignKey('wikigesu.Localisation', blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.style, self.provenance)

