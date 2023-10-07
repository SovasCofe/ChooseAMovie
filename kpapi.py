from KinoPoiskAPI.kinopoisk_api import KP


kinopoisk = KP(token='1bd9cad4-b605-40e1-8515-5ef734152414')


search = kinopoisk.search('Леон')

for item in search:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))