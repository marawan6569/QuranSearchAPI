# QuranSearchAPI
search API for quran

## methodes:
### [all_verses_api](https://quran-search-api.herokuapp.com/api/allVerses):
- returns all verses of quran
---
        
###  [search_api](https://quran-search-api.herokuapp.com/api/search/عريض):
- it takes string then returns all verses that containse this string;
- for example if i sent  "عريض" it returnes :
```json
{
  "resultsLength": 1,
  "data": [
    {
      "verse_pk": "S041V051",
      "page": 482,
      "hizbQuarter": 193,
      "juz": 25,
      "verse": "وَإِذَا أَنْعَمْنَا عَلَى الْإِنسَانِ أَعْرَضَ وَنَأَىٰ بِجَانِبِهِ وَإِذَا مَسَّهُ الشَّرُّ فَذُو دُعَاءٍ عَرِيضٍ",
      "verseWithoutTashkeel": "وإذا أنعمنا على الإنسان أعرض ونأى بجانبه وإذا مسه الشر فذو دعاء عريض",
      "numberInSurah": 51,
      "numberInQuran": 4269,
      "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/4269",
      "audio1": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4269.mp3",
      "audio2": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4269.mp3",
      "sajda": false
    }
  ]
}
```
---
### [get_surah_api](https://quran-search-api.herokuapp.com/api/getSurah/1):
- it takes surah number then returns all verses in this surah
- surahs numbers between 1:114.
---
### [get_verse_api](https://quran-search-api.herokuapp.com/api/getVerse/1/1):
- it takes surah number and verse number then returnes this verse:
- for example if i sent 1 and 1 it returns  frist verse of surah elfateha:
```json
{
  "data": {
    "verse_pk": "S001V001",
    "page": 1,
    "hizbQuarter": 1,
    "juz": 1,
    "verse": "﻿بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    "verseWithoutTashkeel": "﻿بسم الله الرحمن الرحيم",
    "numberInSurah": 1,
    "numberInQuran": 1,
    "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/1",
    "audio1": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/1.mp3",
    "audio2": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/1.mp3",
    "sajda": false
  }
}
```
---
### [get_range_of_verses_api](https://quran-search-api.herokuapp.com/api/getRangeOfVerses/1/10):
- it returns range of verses by taking start and end of this range.
- verses in quran starts from 1 to 6236
---
### [verse_starts_with](https://quran-search-api.herokuapp.com/api/magicSearch/verseStartsWith/د):
- it takes string then returnes all verses that starts with this string.
- for example if i sent "دحورا" it returnes:
```json
{
    "resultLength": 1,
    "data": [
        {
            "verse_pk": "S037V009",
            "page": 446,
            "hizbQuarter": 178,
            "juz": 23,
            "verse": "دُحُورًا ۖ وَلَهُمْ عَذَابٌ وَاصِبٌ",
            "verseWithoutTashkeel": "دحورا  ولهم عذاب واصب",
            "numberInSurah": 9,
            "numberInQuran": 3797,
            "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/3797",
            "audio1": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/3797.mp3",
            "audio2": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/3797.mp3",
            "sajda": false
        }
    ]
}
```
--- 
### [verse_ends_with](https://quran-search-api.herokuapp.com/api/magicSearch/verseEndsWith/ض):
- it take string then returnes all verses that ends with this sring:
- for example if i sent "ض" it returnes:
```json
{
    "resultLength": 1,
    "data": [
        {
            "verse_pk": "S041V051",
            "page": 482,
            "hizbQuarter": 193,
            "juz": 25,
            "verse": "وَإِذَا أَنْعَمْنَا عَلَى الْإِنسَانِ أَعْرَضَ وَنَأَىٰ بِجَانِبِهِ وَإِذَا مَسَّهُ الشَّرُّ فَذُو دُعَاءٍ عَرِيضٍ",
            "verseWithoutTashkeel": "وإذا أنعمنا على الإنسان أعرض ونأى بجانبه وإذا مسه الشر فذو دعاء عريض",
            "numberInSurah": 51,
            "numberInQuran": 4269,
            "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/4269",
            "audio1": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4269.mp3",
            "audio2": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4269.mp3",
            "sajda": false
        }
    ]
}
```
