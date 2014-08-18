from wikigesu.models.piece import Piece
from rest_framework import serializers

class PieceSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = Piece