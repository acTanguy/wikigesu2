
from django.db import models

class Role(models.Model):
    class Meta:
        app_label="wikigesu"

    role = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u"{0}".format(self.role)
