# jisho-downloader
Jisho Downloader, supply it with a txt file (default name is kanji.txt) with words divided in newlines and it will generate another txt file with their readings, definitions and JLPT level.
In case some word in the list is not in the dictionary, or for some reason there's no data for it, the program will generate a second txt file with the list of kanji that couldn't obtain data from

I'd like to create a version of this code, maybe I'll call it "offline jisho downloader". It would search the words directly from a local json file. This way you could load the entire JMdict dictionary (What jisho.org uses) and you could search it offline, which I think should improve the search speed, but unfortunately I don't know how to do that. I would appreciate some help.
