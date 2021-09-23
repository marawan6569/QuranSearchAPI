from .models import Verses
from .serializers import VersesSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def all_verses_api(request) -> None:
    """
        returns all verses.
        not effective, it takes long time to return all verses.
        use it if you want to clone DB or something like that
    """
    verses = Verses.objects.all()
    data = VersesSerializers(verses, many=True).data
    return Response({'length': len(data), 'data': data})

@api_view(['GET'])
def search_api(request, keyWords) -> str:
    """
        search in verses with given keywords
        to return all verses that contains keywords.
    """
    verses = Verses.objects.filter(
        Q(verse__icontains=keyWords) | Q(verseWithoutTashkeel__icontains=keyWords)
    )
    data = VersesSerializers(verses, many=True).data
    return Response({'resultsLength': len(data), 'data': data})

@api_view(['GET'])
def get_surah_api(request, id) -> int:
    """
        takes surah id and returns its verses.
        search in DB with verse_pk.
        verse_pk: S***V***
        it takes id and convert it to first part of verse_pk (S***)
        then search in DB with it with icontains
    """
    SId = f"S{str(id).zfill(3)}"
    verses =Verses.objects.filter(verse_pk__icontains=SId)
    data = VersesSerializers(verses, many=True).data
    return Response({'versesNumber': len(data), 'data': data})

@api_view(['GET'])
def get_verse_api(requst, surahId, verseNum) -> int:
    """
        it takes to integers first is surah id and the second is verse number
        and convert them to verse_pk then search in DB with it with
        get_object_or_404.
    """
    verse_pk = f'S{str(surahId).zfill(3)}V{str(verseNum).zfill(3)}'
    verse = get_object_or_404(Verses, verse_pk=verse_pk)
    data= VersesSerializers(verse).data
    return Response({'data': data})


@api_view(['GET'])
def get_range_of_verses_api(request, start, end) -> int:
    """
        it takes two integer arguments first is the start and second is the end.
        then make start is the smallest number and the end is the biggest.
        and then search with them in numberInQuran with range to return
        list contains slice of verse starts with start value and ends with end value
    """
    values = [start, end]
    start = min(values)
    end = max(values)
    verses = Verses.objects.filter(
        Q(numberInQuran__range=(start, end))
    )
    data = VersesSerializers(verses, many=True).data
    return Response({'resultLength': len(data), 'data': data})

#----------------------- magic search ----------------------

@api_view(['GET'])
def verse_starts_with(request, litters) -> str:
    """
        it takes one str argument and take copy of it and add space to
        first of it because there was an bug in DB in field
        verseWithoutTashkeel if the verse was a start of hizb Quarter
        i removed hizb quarter sign but i found that there was a space between
        hizb quarter sign and the verse, that means some verses start with space not
        litter, if i updated DB i will edit this words
        --------------------who it works?---------------------
        take argument litters and check if verse or verseWithoutTshkeel starts with it
        or versesWithoutTshkeel starts with littersWithSpace
    """
    littersWithSpace = f' {litters}'
    verse = Verses.objects.filter(
        Q(verse__startswith=litters) |
        Q(verseWithoutTashkeel__startswith=litters) |
        Q(verseWithoutTashkeel__startswith=littersWithSpace)

    )

    data = VersesSerializers(verse, many=True).data
    return Response({'resultLength': len(data), 'data': data})

