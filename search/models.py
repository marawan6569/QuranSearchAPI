from django.db import models

# Create your models here.

class Verses(models.Model):
    verse_pk = models.CharField(max_length=8, null=False, blank=False, unique=True, verbose_name='Verse primary key')
    page = models.PositiveIntegerField(null=False, blank=False, verbose_name='Page Number')
    hizbQuarter = models.PositiveIntegerField(null=False, blank=False, verbose_name='Hizb Quarter Number')
    juz = models.PositiveIntegerField(null=False, blank=False, verbose_name='Juz Number')
    verse = models.CharField(max_length=5000, null=False, blank=False, verbose_name='Verse')
    verseWithoutTashkeel = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Verse Without Tashkeel')
    numberInSurah = models.PositiveIntegerField(null=False, blank=False, verbose_name='Verse number in Surah')
    numberInQuran = models.PositiveIntegerField(null=False, blank=False, unique=True, verbose_name='Verse number in Quran')
    audio = models.URLField(null=False, blank=False, unique=True, verbose_name='Audio primary source')
    audio1 = models.URLField(null=True, blank=True, unique=True, verbose_name='Audio 1st secondary source')
    audio2 = models.URLField(null=True, blank=True, unique=True, verbose_name='Audio 2nd secondary source')
    sajda = models.BooleanField(verbose_name='Is Verse sajda')

    class Meta:
        ordering = ['verse_pk']
    def __str__(self):
        return self.verse[:50]
