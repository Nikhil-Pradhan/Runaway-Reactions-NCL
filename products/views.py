from django.shortcuts import render
from django.db import connection
from .models import *

cursor = connection.cursor()


def home(request):
    reactions = Reactions.objects.all()
    context = {"reactions": reactions}
    return render(request, 'home.html', context)
