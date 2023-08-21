
class Clovek:
    def tiskni(self): #nechci aby mela parametry, potrebuju odkazat na parametry pepy, ktere jeste nemam
            #kazda metoda v pythonu musi mit aspon jeden parametr - self
        print(f"Jmeno : {self.jmeno}, vek : {self.vek}")

pepa = Clovek() #vytvarim instance, zavolam jakobych zavolal funkci 
pepa.jmeno = "Josef" #instancni promena, pepa ma svoji, lojza ma svoji
pepa.vek = 10

pepa.tiskni() #vlozi sam sebe
Clovek.tiskni(pepa) #stejny

lojza = Clovek()

