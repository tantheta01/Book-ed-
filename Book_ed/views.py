from django.shortcuts import render
from django.http import HttpResponse

def interface(request):
	return HttpResponse("Welcome to Book-ed!\nPlease select the book you like\n")


# Create your views here.
