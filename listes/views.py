from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    return render(request, 'listes/index.html')


def login(request):
    return render(request, 'listes/login.html')