import threading, time

def citac():
    c=1
    while True:
        print(f"Citac : {c}")
        c+=1
        time.sleep(1)

# citac() #takhle nikdy neskonci

vlakno = threading.Thread(target=citac) # vytvori vlakno z funkce

vlakno.start()

print ("Pokracuje dal .....")