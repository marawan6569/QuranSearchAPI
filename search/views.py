from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Verses

# Create your views here.

def viweAll(request):
    verses = Verses.objects.all()
    verses = {'verses': verses}
    return render(request, 'search/search.html', verses)

def searchByWords(requeat):
    keyWords = requeat.POST.get('ayah')
    if keyWords:
        verses = Verses.objects.filter(
            Q(verse__icontains=keyWords) | Q(verseWithoutTashkeel__icontains=keyWords)
        )
        verses = {'verses': verses}
        return render(requeat, 'search/search.html', verses)
    else:
        return viweAll(requeat)

def getSurah(request, id):
    SId = f"S{str(id).zfill(3)}"
    surah = Verses.objects.filter(
        Q(verse_pk__icontains=SId)
    )
    verses = {'verses': surah}
    return render(request, 'search/search.html', verses)

def api_docs(request):
    return render(request, 'search/api.html')