import sqlite3

with sqlite3.connect("data.sqlite3") as conn: #tady jen jmeno souboru, kdyby plnohodnota database tak dalsi parametry jako ip user pasw a dalsi ....
    cur = conn.cursor() #v ramci jednoho connection muzu vytvorit vice

    # 1 step
    # cur.execute("create table seznam (jemno char(100), cislo char(20))") # execute metoda kterou spustime nad kurzorem, kterj ma tvar sql prikazu
        #muzu pusti jen jednou
        #pozor typo in jmeno - napsal jsem jemno
 
# #2 step
#     for i in range(50):
#         cur.execute(f"insert into seznam values ('jmeno{i}','cislo{i}')")

    cur.execute("select jemno, cislo from seznam")
    
    # for zaznam in cur:
    #     #zalezi co ten zaznam bude zac, v nasem pripade dvouprvkove pole
    #     print(f"Jmeno : {zaznam[0]}, cislo : {zaznam[1]}")

    print(cur.fetchall()) #vratil by nam vsechno jako pole poli


    conn.commit() #aby se ty zmeny provedly