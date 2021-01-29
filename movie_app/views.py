from django.shortcuts import render
from movie_app.models import Movies

def index(request):
    movies = Movies.objects.all()
    return render(request, 'index.html', {'movies':movies})
