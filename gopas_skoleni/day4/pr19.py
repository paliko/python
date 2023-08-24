
# s = open("data.txt", mode="r", encoding="utf8") #mode a encoding nepovinne
# s.close()

#misto s.close:

with open("data.txt", mode="r", encoding="utf8") as s1, open("data.bak", mode="w", encoding="utf8") as s2:
    #mode a - kdyz existuje tak ho nesmaze ale prida
    #mode rb - vracel by posloupnost bytu a ne stringu, melo by smysl kdyby se nejednalo o textovej soubor
    for radek in s1:
        print(radek.strip())
        s2.write(radek)
    
