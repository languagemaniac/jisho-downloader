import requests


def datos_kanji(info, current_kanji):
    print("\n")
    print(current_kanji)
    try:
        reading = info['japanese'][0]['reading']
    except:
        reading = "No Reading"
    print("Reading" + str(reading))

    try:
        meaning = info['senses'][0]['english_definitions']
    except:
        meaning = "No Meaning"
    print("Reading" + str(meaning))

    try:
        jlpt = info['jlpt']
    except:
        jlpt = "No jlpt"
    print(jlpt)

    print(str(current_kanji.rstrip()) + "\t" + str(reading) + "\t" + str(meaning) + "\t" + str(jlpt) + "\n")
    print("\n")
    return str(current_kanji.rstrip()) + "\t" + str(reading) + "\t" + str(meaning) + "\t" + str(jlpt) + "\n"


if __name__ == '__main__':
    words_file = "kanji.txt"
    save_meaning = "meaning.txt"
    error_meaning = "error_meaning.txt"
    m_file = open(save_meaning, "w", encoding='utf-8')
    e_file = open(error_meaning, "w", encoding='utf-8')
    total = 0
    with open(words_file, "r", encoding='utf-8') as fp:
        for count, line in enumerate(fp):
            pass
        print('Total Lines', count + 1)
        total = count + 1
    with open(words_file, "r", encoding='utf-8') as f:
        count = 0
        for kanji in f:
            response = requests.get("https://jisho.org/api/v1/search/words?keyword='" + kanji + "'")
            try:
                json = response.json()
                if response.status_code == 200:
                    #print(len(json['data']))
                    if len(json['data']) > 0:
                        m_file.write(datos_kanji(json['data'][0], kanji))
            except:
                print("Error con " + str(kanji))
                e_file.write(str(kanji))
            count += 1
            #print("Realizado el %.1f" % ((count/total)*100) + "%. Se han procesado " + str(count) + "/" + str(total) + " palabras.")

    print("KANJIS: PROCESO COMPLETADO")
    m_file.close()
    e_file.close()
    f.close()
