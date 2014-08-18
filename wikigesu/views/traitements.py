from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from wikigesu.models.message import Message
from wikigesu.models.piece import Piece
from wikigesu.models.utilisateur import UtilisateurProfile

def ajoutCommentaire(request):
	message = request.POST.get("message")
	piece = Piece.objects.get(pk=request.POST.get("piece"))
	mesure = request.POST.get("measure")
	voice = request.POST.get("voice")
	if request.user.is_authenticated():
		try:
			posteur = request.user.utilisateurprofile
		except UtilisateurProfile.DoesNotExist:
			posteur = None
	else:
		posteur = None
	ip = get_client_ip(request)
	if request.method == 'POST':
		if 'file' in request.FILES:
			com = Message(posteur=posteur, message=message, piece=piece, voix=voice, mesure=mesure, ip=ip, fichier=request.FILES['file'])
		else:
			com = Message(posteur=posteur, message=message, piece=piece, voix=voice, mesure=mesure, ip=ip)
	else:
		com = Message(posteur=posteur, message=message, piece=piece, voix=voice, mesure=mesure, ip=ip)
	com.save()
	return HttpResponse(com.id);
	

def valideCommentaire(request):
	if request.user.has_perm("valider_message"):
		com = Message.objects.get(pk=request.POST.get('id'))
		com.validee = True
		com.save()
		return HttpResponse(request.POST.get('id'))
	else:
		return HttpResponse("-1")

def refuseCommentaire(request):
	if request.user.has_perm("valider_message"):
		com = Message.objects.get(pk=request.POST.get('id'))
		com.delete()
		return HttpResponse(request.POST.get('id'))
	else:
		return HttpResponse("-1")

def archiveCommentaire(request):
	if request.user.has_perm("archiver_message"):
		com = Message.objects.get(pk = request.POST.get('id'))
		com.archive = True
		com.save()
		return HttpResponse(request.POST.get('id'))
	else:
		return HttpResponse("-1")

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
