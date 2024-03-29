from django.urls import path
from .views import *
from .api_views import *

app_name = 'search'

urlpatterns = [
    path('', api_docs, name='viweAll'),
    path('search/', searchByWords, name='searchByWords'),
    path('surah/<int:id>/', getSurah, name='getSurah'),
    ################## API ##########################
    path('api/', api_docs, name='apiDocs'),
    path('api/allVerses/', all_verses_api, name='versesListAPI'),
    path('api/search/<str:keyWords>/', search_api, name='searchAPI'),
    path('api/getSurah/<int:id>/', get_surah_api, name='getSurahAPI'),
    path('api/getVerse/<int:surahId>/<int:verseNum>/', get_verse_api, name='getVerseAPI'),
    path('api/getRangeOfVerses/<int:start>/<int:end>/', get_range_of_verses_api, name='getRangeOfVerses'),
    path('api/magicSearch/verseStartsWith/<str:letters>/', verse_starts_with, name='verseStartsWithAPI'),
    path('api/magicSearch/verseEndsWith/<str:letters>/', verse_ends_with, name='verseEndsWithAPI'),
]
