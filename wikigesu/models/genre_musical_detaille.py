from django.db import models


class GenreMusicalDetaille(models.Model):
    class Meta:
        app_label="wikigesu"
        verbose_name = "Genre Musical Detaille"
        verbose_name_plural = "Genres Musicaux Detailles"

    MADRIGAL = 'Madrigal'
    MOTET = 'Motet'
    MESSE = 'Messe'
    CANZONE = 'Canzone'
    CANTATE = 'Cantate'
    CHANSON = 'Chanson'

    CHOIX_GENRE = (
        (MADRIGAL, 'Madrigal'),
        (MOTET, 'Motet'),
        (MESSE, 'Messe'),
        (CANZONE, 'Canzone'),
        (CANTATE, 'Cantate'),
        (CHANSON, 'Chanson'),
    )

    genre_musical = models.CharField(max_length=255, choices=CHOIX_GENRE, default=None, unique=True)

    def __unicode__(self):
        return u"{0}".format(self.genre_musical)

