from django.contrib import admin
from  .models import Verses
# Register your models here.

class ModelVerses(admin.ModelAdmin):

    list_display = ['__str__', 'verse_pk', 'numberInQuran', 'page', 'hizbQuarter', 'juz', 'sajda']
    search_fields = ['verse', 'verseWithoutTashkeel']

admin.site.register(Verses, ModelVerses)
