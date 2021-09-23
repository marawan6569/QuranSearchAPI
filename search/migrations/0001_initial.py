# Generated by Django 3.2.7 on 2021-09-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse_pk', models.CharField(max_length=8, unique=True, verbose_name='Verse primary key')),
                ('page', models.IntegerField(verbose_name='Page Number')),
                ('hizbQuarter', models.IntegerField(verbose_name='Hizb Quarter Number')),
                ('juz', models.IntegerField(verbose_name='Juz Number')),
                ('verse', models.CharField(max_length=5000, verbose_name='Verse')),
                ('verseWithoutTaskeel', models.CharField(max_length=1000, verbose_name='Verse Without Tashkeel')),
                ('numberInSurah', models.IntegerField(verbose_name='Verse number in Surah')),
                ('numberInQuran', models.IntegerField(verbose_name='Verse number in Quran')),
                ('audio', models.URLField(unique=True, verbose_name='Audio primary source')),
                ('audio1', models.URLField(blank=True, null=True, unique=True, verbose_name='Audio 1st secondary source')),
                ('audio2', models.URLField(blank=True, null=True, unique=True, verbose_name='Audio 2nd secondary source')),
                ('sajda', models.BooleanField(verbose_name='Is Verse sajda')),
            ],
        ),
    ]
