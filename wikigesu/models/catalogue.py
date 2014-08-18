from django.db import models


class Catalogue(models.Model):
    class Meta:
        app_label="wikigesu"

    RISM_A = 'RISM_A'
    RISM_B = 'RISM_B'
    CENSUS = 'CENSUS'
    VOGEL = 'VOGEL'
    BROWN = 'BROWN'
    HEARTZ = 'HEARTZ'
    VANHULST = 'VANHULST'
    LESURE = 'LESURE'
    POGUE = 'POGUE'
    AGEE = 'AGEE'
    BERNSTEIN = 'BERNSTEIN'
    BOETTICHER = 'BOETTICHER'
    BOORMAN = 'BOORMAN'
    GUILLO = 'GUILLO'
    LEWIS = 'LEWIS'
    SARTORI = 'SARTORI'
    WEAVER = 'WEAVER'
    PATALAS ='PATALAS'
    GOOVEARTS = 'GOOVEARTS'

    CHOIX_CATALOGUE = (
        (RISM_A, 'Rism A'),
        (RISM_B, 'Rism B'),
        (CENSUS,'Census'),
        (VOGEL,'Vogel'),
        (BROWN,'Brown'),
        (HEARTZ,'Hearz'),
        (VANHULST,'Vanhulst'),
        (LESURE,'Lesure'),
        (POGUE,'Pogue'),
        (AGEE,'Agee'),
        (BERNSTEIN,'Bernstein'),
        (BOETTICHER,'Boetticher'),
        (BOORMAN,'Boorman'),
        (GUILLO,'Guillo'),
        (LEWIS,'Lewis'),
        (SARTORI,'Sartori'),
        (WEAVER,'Weaver'),
        (PATALAS, 'Patalas'),
        (GOOVEARTS, 'Goovearts'),
    )


    choix_catalogue = models.CharField(max_length=10, choices=CHOIX_CATALOGUE, default=RISM_A )
    identifiant = models.CharField(max_length=32, blank=True, null=True, unique=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.identifiant, self.choix_catalogue)

    def cote(self):
	return u"{0} : {1}".format(self.choix_catalogue, self.identifiant)
