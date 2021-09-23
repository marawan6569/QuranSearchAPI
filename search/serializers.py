from dataclasses import fields

from rest_framework import serializers
from .models import Verses

class VersesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Verses
        fields = [
            'verse_pk',
            'page',
            'hizbQuarter',
            'juz',
            'verse',
            'verseWithoutTashkeel',
            'numberInSurah',
            'numberInQuran',
            'audio',
            'audio1',
            'audio2',
            'sajda',
        ]