from wikigesu.models.recueil import Recueil
from rest_framework import serializers

class RecueilSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = Recueil