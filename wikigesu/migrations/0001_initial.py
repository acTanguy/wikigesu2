# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotheque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_normalise', models.CharField(max_length=255, null=True, blank=True)),
                ('sigle_rism', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choix_catalogue', models.CharField(default=b'RISM_A', max_length=10, choices=[(b'RISM_A', b'Rism A'), (b'RISM_B', b'Rism B'), (b'CENSUS', b'Census'), (b'VOGEL', b'Vogel'), (b'BROWN', b'Brown'), (b'HEARTZ', b'Hearz'), (b'VANHULST', b'Vanhulst'), (b'LESURE', b'Lesure'), (b'POGUE', b'Pogue'), (b'AGEE', b'Agee'), (b'BERNSTEIN', b'Bernstein'), (b'BOETTICHER', b'Boetticher'), (b'BOORMAN', b'Boorman'), (b'GUILLO', b'Guillo'), (b'LEWIS', b'Lewis'), (b'SARTORI', b'Sartori'), (b'WEAVER', b'Weaver'), (b'PATALAS', b'Patalas'), (b'GOOVEARTS', b'Goovearts')])),
                ('identifiant', models.CharField(max_length=32, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cote_exemplaire', models.CharField(max_length=16, null=True, blank=True)),
                ('etat', models.CharField(default=b'COMPLET', max_length=9, choices=[(b'COMPLET', b'Complet'), (b'INCOMPLET', b'Incomplet')])),
                ('remarques', models.TextField(null=True, blank=True)),
                ('lien_source', models.URLField(null=True, blank=True)),
                ('localisation', models.ForeignKey(blank=True, to='wikigesu.Bibliotheque', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(unique=True, max_length=255, blank=True)),
                ('attachment', models.FileField(upload_to=b'partitions')),
            ],
            options={
                'verbose_name': b'File',
                'verbose_name_plural': b'Files',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenreMusicalDetaille',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_musical', models.CharField(default=None, unique=True, max_length=255, choices=[(b'Madrigal', b'Madrigal'), (b'Motet', b'Motet'), (b'Messe', b'Messe'), (b'Canzone', b'Canzone'), (b'Cantate', b'Cantate'), (b'Chanson', b'Chanson')])),
            ],
            options={
                'verbose_name': b'Genre Musical Detaille',
                'verbose_name_plural': b'Genres Musicaux Detailles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenreMusicalNormalise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(default=b'profane', max_length=128, choices=[(b'profane', b'Profane'), (b'religieux', b'Religieux')])),
            ],
            options={
                'verbose_name': b'Genre Musical Normalise',
                'verbose_name_plural': b'Genres Musicaux Normalises',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pays_normalise_langue', models.CharField(max_length=255)),
                ('pays_francais', models.CharField(max_length=255)),
                ('nom_ville_normalise_langue', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('nom_ville_francais', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('nom_ville_source', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='genremusicalnormalise',
            name='provenance',
            field=models.ForeignKey(blank=True, to='wikigesu.Localisation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bibliotheque',
            name='localisation',
            field=models.ForeignKey(to='wikigesu.Localisation'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('voix', models.CharField(max_length=10)),
                ('mesure', models.SmallIntegerField()),
                ('validee', models.BooleanField(default=False)),
                ('archive', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField()),
                ('fichier', models.FileField(null=True, upload_to=b'fichiers_utilisateur')),
            ],
            options={
                'permissions': ((b'valider_message', b'Peut valider les messages'), (b'archiver_message', b'Peut archiver les messages')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255, null=True, blank=True)),
                ('prenom', models.CharField(max_length=255, null=True, blank=True)),
                ('variante_nom', models.CharField(max_length=255, null=True, blank=True)),
                ('nom_bref', models.CharField(max_length=255, null=True, blank=True)),
                ('date_naissance', models.CharField(max_length=16, null=True, blank=True)),
                ('date_mort', models.CharField(max_length=16, null=True, blank=True)),
                ('periode_activite', models.CharField(max_length=16, null=True, blank=True)),
                ('bibliographie', models.TextField(null=True, blank=True)),
                ('remarques', models.TextField(null=True, blank=True)),
                ('lieu_activite', models.ManyToManyField(to='wikigesu.Localisation', null=True, blank=True)),
                ('lieu_mort', models.ForeignKey(blank=True, to='wikigesu.Localisation', null=True)),
                ('lieu_naissance', models.ForeignKey(blank=True, to='wikigesu.Localisation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(unique=True, null=True, blank=True)),
                ('titre', models.CharField(max_length=255)),
                ('place_dans_recueil', models.IntegerField(max_length=4, null=True, blank=True)),
                ('nombre_de_voix', models.IntegerField(max_length=4, null=True, blank=True)),
                ('pdf_link', models.URLField(null=True, blank=True)),
                ('mei_link', models.URLField(null=True, blank=True)),
                ('mp3_link', models.URLField(null=True, blank=True)),
                ('remarques', models.TextField(null=True, blank=True)),
                ('compositeur', models.ForeignKey(blank=True, to='wikigesu.Personne', null=True)),
                ('concordance_imp', models.ManyToManyField(to='wikigesu.Piece', null=True, blank=True)),
                ('concordance_ms', models.ManyToManyField(to='wikigesu.Piece', null=True, blank=True)),
                ('fichiers_joints', models.ManyToManyField(to='wikigesu.File', null=True, blank=True)),
                ('genre_musical_detaille', models.ForeignKey(blank=True, to='wikigesu.GenreMusicalDetaille', null=True)),
                ('genre_musical_normalise', models.ForeignKey(blank=True, to='wikigesu.GenreMusicalNormalise', null=True)),
                ('poete', models.ForeignKey(blank=True, to='wikigesu.Personne', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='piece',
            field=models.ForeignKey(to='wikigesu.Piece'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Recueil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.SlugField(unique=True, null=True, blank=True)),
                ('titre', models.CharField(max_length=255, null=True, blank=True)),
                ('recueil_id', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('titre_traduit', models.CharField(max_length=255, null=True, blank=True)),
                ('support', models.CharField(default=b'imprime', max_length=9, choices=[(b'manuscrit', b'manuscrit'), (b'imprime', b'imprime')])),
                ('datation', models.IntegerField(max_length=4, null=True, blank=True)),
                ('nombre_pieces', models.IntegerField(max_length=4, null=True, blank=True)),
                ('remarques', models.TextField(null=True, blank=True)),
                ('catalogue_id', models.ManyToManyField(to='wikigesu.Catalogue', null=True, blank=True)),
                ('compositeurs', models.ManyToManyField(to='wikigesu.Personne', null=True, blank=True)),
                ('editeur_scientifique', models.ManyToManyField(to='wikigesu.Personne', null=True, blank=True)),
                ('genre_musical_detaille', models.ManyToManyField(to='wikigesu.GenreMusicalDetaille', null=True, blank=True)),
                ('genre_musical_normalise', models.ManyToManyField(to='wikigesu.GenreMusicalNormalise', null=True, blank=True)),
                ('libraire', models.ManyToManyField(to='wikigesu.Personne', null=True, blank=True)),
                ('reedition', models.ManyToManyField(to='wikigesu.Recueil', null=True, blank=True)),
                ('ville_edition', models.ForeignKey(blank=True, to='wikigesu.Localisation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='piece',
            name='recueil_id',
            field=models.ForeignKey(to_field=b'recueil_id', blank=True, to='wikigesu.Recueil', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exemplaire',
            name='recueil_id',
            field=models.ForeignKey(to_field=b'recueil_id', blank=True, to='wikigesu.Recueil', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personne',
            name='role',
            field=models.ManyToManyField(to='wikigesu.Role', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Texte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, null=True, blank=True)),
                ('item', models.SlugField(null=True, blank=True)),
                ('titre_traduit', models.CharField(max_length=255, null=True, blank=True)),
                ('recueil_litteraire', models.CharField(max_length=255, null=True, blank=True)),
                ('forme_litteraire', models.CharField(max_length=255, null=True, blank=True)),
                ('rimes', models.CharField(max_length=255, null=True, blank=True)),
                ('corps_texte', models.TextField(null=True, blank=True)),
                ('remarques', models.TextField(null=True, blank=True)),
                ('source', models.URLField(null=True, blank=True)),
                ('auteur', models.ForeignKey(blank=True, to='wikigesu.Personne', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='piece',
            name='texte',
            field=models.ForeignKey(blank=True, to='wikigesu.Texte', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UtilisateurProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Utilisateur', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('personne', models.ForeignKey(blank=True, to='wikigesu.Personne', help_text=b'Lie ce compte a un utilisateur', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='posteur',
            field=models.ForeignKey(blank=True, to='wikigesu.UtilisateurProfile', null=True),
            preserve_default=True,
        ),
    ]
