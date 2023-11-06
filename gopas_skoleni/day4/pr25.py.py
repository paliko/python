import urllib.request

with urllib.request.urlopen("http://www.idnes.cz/") as server: #vraci se nam objekt, textovej soubor ale budou to bajty
    for radek in server:
        print(str(radek,encoding="cp1250").strip()) #prevod batu na format stringu (na seznamu.cz jim nefungovalo codovani utf8)
