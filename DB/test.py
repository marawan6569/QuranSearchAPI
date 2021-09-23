import sqlite3

quranDB = sqlite3.connect('../DB/quran.db')
quranCR = quranDB.cursor()
for  i in range(1, 6237):
    id = i
    page = quranCR.execute(f'SELECT page FROM verses WHERE id == {id} ').fetchall()[0][0]
    quarter = quranCR.execute(f'SELECT hizbQuarter FROM verses WHERE id == {id} ').fetchall()[0][0]
    juz = quranCR.execute(f'SELECT juz FROM verses WHERE id == {id} ').fetchall()[0][0]
    surahID = quranCR.execute(f'SELECT surah FROM verses WHERE id == {id} ').fetchall()[0][0]
    ayah = quranCR.execute(f'SELECT verse FROM verses WHERE id == {id} ').fetchall()[0][0]
    ayahWithoutTashkeel = quranCR.execute(f'SELECT verseWithoutTaskeel FROM verses WHERE id == {id} ').fetchall()[0][0]
    ayahNumInSurah = quranCR.execute(f'SELECT numberInSurah FROM verses WHERE id == {id} ').fetchall()[0][0]
    ayahNumInQuran = quranCR.execute(f'SELECT numberInQuran FROM verses WHERE id == {id} ').fetchall()[0][0]
    paudio = quranCR.execute(f'SELECT audio FROM verses WHERE id == {id} ').fetchall()[0][0]
    saudio1 = quranCR.execute(f'SELECT audio1 FROM verses WHERE id == {id} ').fetchall()[0][0]
    saudio2 = quranCR.execute(f'SELECT audio2 FROM verses WHERE id == {id} ').fetchall()[0][0]
    sajda = quranCR.execute(f'SELECT sajda FROM verses WHERE id == {id} ').fetchall()[0][0]
    ayah_pk =  f'S{str(surahID).zfill(3)}V{str(ayahNumInSurah).zfill(3)}'

    DjDB = sqlite3.connect('db.sqlite3')
    cr = DjDB.cursor()
    cr.execute(f'''INSERT INTO search_verses(verse_pk, page, hizbQuarter, juz, verse, verseWithoutTaskeel, numberInSurah, numberInQuran, audio, audio1, audio2, sajda) VALUES ("{ayah_pk}", {page}, {quarter}, {juz}, "{ayah}", "{ayahWithoutTashkeel}", {ayahNumInSurah}, {ayahNumInQuran}, "{paudio}", "{saudio1}", "{saudio2}", {sajda})''')

    DjDB.commit()

    print('=' * 50)
    print(ayah_pk, '|', page, '|', quarter, '|', juz, '|', surahID, '|', ayah, '|', ayahWithoutTashkeel, '|', ayahNumInSurah, '|', ayahNumInQuran, '|', paudio, '|', saudio1, '|', saudio2, '|', sajda)

DjDB.close()