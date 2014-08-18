from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from wikigesu.models.localisation import Localisation
from wikigesu.models.bibliotheque import Bibliotheque
from wikigesu.models.role import Role
from wikigesu.models.personne import Personne

from wikigesu.models.recueil import Recueil
from wikigesu.models.genre_musical_normalise import GenreMusicalNormalise
from wikigesu.models.genre_musical_detaille import GenreMusicalDetaille
from wikigesu.models.exemplaire import Exemplaire
from wikigesu.models.catalogue import Catalogue
from wikigesu.models.piece import Piece
from wikigesu.models.file import File
from wikigesu.models.message import Message
from wikigesu.models.utilisateur import UtilisateurProfile
from wikigesu.models.texte import Texte

def reindex_in_solr(modeladmin, request, queryset):
    # calls the save method on every item, ensuring the
    # post_save handler is called
    for item in queryset:
        print(item)
        item.save()
    reindex_in_solr.short_description = "Re-Index Selected Items"

class LocalisationAdmin(admin.ModelAdmin):
    pass

class BibliothequeAdmin(admin.ModelAdmin):
    pass

class RoleAdmin(admin.ModelAdmin):
    pass

class PersonneAdmin(admin.ModelAdmin):
    pass

class TexteAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]   

class ReceuilAdmin(admin.ModelAdmin):
    list_display = ('titre', 'recueil_id')
    filter_horizontal=('compositeurs', 'genre_musical_normalise', 'genre_musical_detaille')
    actions = [reindex_in_solr]    
    

class FilePieceInline(admin.TabularInline):
    model = Piece.fichiers_joints.through
    can_delete = True,
    verbose_name = "File"
    verbose_name_plural = "Files"

class PieceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'recueil_id', 'place_dans_recueil')
    list_filter = ('recueil_id',)
    filter_horizontal=('concordance_ms', 'concordance_imp', )
    inlines = (
	FilePieceInline,
    )
    exclude = ('fichiers_joints'),
    actions = [reindex_in_solr]

class GenreMusicalNormaliseAdmin(admin.ModelAdmin):
    pass

class GenreMusicalDetailleAdmin(admin.ModelAdmin):
    pass

class ExemplaireAdmin(admin.ModelAdmin):
    list_display = ('localisation','etat')

class CatalogueAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'piece','validee', 'archive')

class UtilisateurInline(admin.StackedInline):
    model = UtilisateurProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (
        UtilisateurInline,
    )

admin.site.register(Localisation, LocalisationAdmin)
admin.site.register(Bibliotheque, BibliothequeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Recueil, ReceuilAdmin)
admin.site.register(GenreMusicalNormalise, GenreMusicalNormaliseAdmin)
admin.site.register(GenreMusicalDetaille, GenreMusicalDetailleAdmin)
admin.site.register(Exemplaire, ExemplaireAdmin)
admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(File)
admin.site.register(Message, MessageAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Texte, TexteAdmin)
