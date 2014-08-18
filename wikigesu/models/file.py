import os
from django.db import models

class File(models.Model):
    class Meta:
        app_label = "wikigesu"
        verbose_name = "File"
        verbose_name_plural = "Files"

    description = models.CharField(max_length=255, blank=True, unique=True)
    attachment = models.FileField(upload_to=os.path.join("partitions"))

    def __unicode__(self):
        return u"{0}".format(self.description)   
