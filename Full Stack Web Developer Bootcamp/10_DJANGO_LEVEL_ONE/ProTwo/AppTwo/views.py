from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<em>My Second App </em>")

def help(request):
    help_dict = {'help_insert': 'This is the help page!'}
    return render(request, 'AppTwo/help.html', context=help_dict)
