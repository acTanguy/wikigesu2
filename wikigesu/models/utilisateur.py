from django.db import models
from django.contrib.auth.models import User

from wikigesu.models.personne import Personne

class UtilisateurProfile(models.Model):
    class Meta:
        app_label = "wikigesu"

    Utilisateur = models.OneToOneField(User, db_index=True, parent_link="pseudo")
    personne = models.ForeignKey(Personne, blank=True, null=True, help_text="Lie ce compte a un utilisateur", db_index=True, related_name="profile")
    def __unicode__(self):
        return self.personne.nom_bref

User.profile = property(lambda u: utilisateurProfile.objects.get_or_create(user=u)[0])
