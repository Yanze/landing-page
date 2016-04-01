from django.http import HttpResponse,  HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'persons': [
            {'name': 'Yanze', 'interest': 'programming', 'favo_language': 'Python, JavaScript, Swift'},
            {'name': 'Zagara', 'interest': 'Play games', 'favo_language': 'Bon sha ka la ka'},
            {'name': 'Artanis', 'interest': 'throw ice', 'favo_language': 'No one can stop me!'},
        ]
    }
    return render(request, 'landing/index.html', context)
