from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wikigesu.models.texte import Texte
from wikigesu.models.recueil import Recueil
from wikigesu.models.exemplaire import Exemplaire
from wikigesu.models.piece import Piece
from wikigesu.models.message import Message

def home(request):
    return render(request, 'main/home.html')

def recueil(request, pk):

    recueil = Recueil.objects.get(recueil_id=pk)
    exemplaires = Exemplaire.objects.filter(recueil_id=pk)
    pieces = Piece.objects.filter(recueil_id=pk)

    return render(request, 'main/recueil.html', {'recueil': recueil, 'exemplaires':exemplaires, 'pieces':pieces})


def recueils(request):
    recueils = Recueil.objects.all().order_by('id') 

    return render(request, 'main/recueils.html', {'recueils': recueils})

def piece(request, recueil, place):
    try:
        piece = Piece.objects.get(recueil_id=(Recueil.objects.get(recueil_id=recueil)), place_dans_recueil=place)
        commentaires = []
	ip = get_client_ip(request)
	print ip
        if request.user.is_authenticated():
	    u = request.user
            if u.has_perm('wikigesu.valider_message'):
                commentaires = Message.objects.filter(piece=piece, archive=False).order_by('-timestamp')
            else:
                commentaires = Message.objects.filter(piece=piece, validee=True, archive=False).order_by('-timestamp') | Message.objects.filter(piece=piece, validee=False, ip=ip).order_by('-timestamp')
        else:
            commentaires = Message.objects.filter(piece=piece, validee=True, ip=ip, archive=False).order_by('-timestamp') | Message.objects.filter(piece=piece, validee=False, ip=ip).order_by('-timestamp')
    except Piece.DoesNotExist:
        raise Http404
    return render(request, 'main/piece.html', {'piece': piece, 'commentaires': commentaires})

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def pieces(request):
    pieces = Piece.objects.all().order_by('recueil_id', 'place_dans_recueil')
    paginator = Paginator(pieces, 25)

    page = request.GET.get('page')
    try:
        all_pieces = paginator.page(page)
    except PageNotAnInteger:
        all_pieces = paginator.page(1)
    except EmptyPage:
        all_pieces = paginator.page(paginator.num_pages)

    return render(request, 'main/pieces.html', {'pieces': all_pieces})

def textes(request):
    textes = Texte.objects.all().order_by('titre')
    paginator = Paginator(textes, 25)

    page = request.GET.get('page')
    try:
        all_textes = paginator.page(page)
    except PageNotAnInteger:
        all_textes = paginator.page(1)
    except EmptyPage:
        all_textes = paginator.page(paginator.num_pages)

    return render(request, 'main/textes.html', {'textes': all_textes})

def texte(request, pk):
    texte = Texte.objects.get(slug=pk)

    return render(request, 'main/texte.html', {'texte':texte})

def equipe(request):
    return render(request, 'main/equipe.html')
