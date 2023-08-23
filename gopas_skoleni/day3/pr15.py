import threading, time

def citac(id):
    c=1
    while True:
        print(f"Citac : {id} - {c}")
        c+=1
        time.sleep(1)

# citac() #takhle nikdy neskonci

vlakno1 = threading.Thread(target=citac,args=(1,)) # vytvori vlakno z funkce
                                                    # kdyby tam nebyla carka (1,) tak by to byl int a ne ntice
vlakno2 = threading.Thread(target=citac,args=(2,)) 

vlakno1.deamon = True
vlakno2.deamon = True

vlakno1.start()
vlakno2.start()



print ("Pokracuje dal .....")