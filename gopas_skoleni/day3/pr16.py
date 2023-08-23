import threading, time

vlakna = []
vysl = []
class Citac(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id=id
        self.deamon=False
    
    def run(self): #to co vytvari ten beh
        c=1
        while True:
            text = (f"Citac : {self.id} - {c}")
            print(text)
            vysl.append(text)
            c+=1
            time.sleep(1)

# Citac je potomek Thread, tu vykonou cas reprezentuje meetoda run

vlakno1 = Citac(1)
vlakno2 = Citac(2)


# vlakno1.start()
# vlakno2.start()


for i in range(3):
    vlakna.append(Citac(i))

for vlakno in vlakna:
    vlakno.start()


print ("Pokracuje dal .....")