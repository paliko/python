import sys

class Clovek:
    def __init__(self, jmeno:str="", vek:int=0): 
        self.jmeno = jmeno
        self.vek = vek

    #kdyz budu chti pracovat s objektem jako retezcem
    def __str__(self): 
        return self.jmeno
    
    def __add__(self,other):
        return self.vek + other.vek
    
    def __lt__(self,other):
        return self.vek<other.vek
    
    def __getitem__(self,item):
        return self.jmeno[item]
    
    def __setitem__(self,key, value):
         print(f"{key}: {value}")   #f formatovaci retezec jinak by vypsalo "{key}: {value}"

    def __call__(self,p): #muzu zkusit ze to vrati sinus
         import math
         return math.sin(p)
    
    def __del__(self):
         print(f"KONEC CLOVEKA: {self.jmeno}")

    def tiskni(self): #nechci aby mela parametry, potrebuju odkazat na parametry pepy, ktere jeste nemam
            #kazda metoda v pythonu musi mit aspon jeden parametr - self, nemusi se to jmenovat self ale je to zvykem
        print(f"Jmeno : {self.jmeno}, vek : {self.vek}")

#pepa = Clovek() #vytvarim instance, zavolam jakobych zavolal funkci 
#nemusim mit, kdyz jsem pridal parametry do init
# pepa.jmeno = "Josef" #instancni promena, pepa ma svoji, lojza ma svoji
# pepa.vek = 10

pepa = Clovek("Josef",20)

pepa.tiskni() #vlozi sam sebe
Clovek.tiskni(pepa) #mohl bych zavolat takhle, trida ma tu funkcic
print(str(pepa)) #technicky prevedeni na retezec -> bude urcite existovat naka magicka metoda, v tomto pripade str
    #bez str vytiskne jen jemno

lojza = Clovek("Aloijz",15)
lojza.tiskni()

print(pepa+lojza)

print(pepa<lojza) #porovnani

print(pepa[3]) #__getitem__
for a in pepa:  #pepa je nyni iterovatelnej
        print(a)


pepa[3]="neco" #set item
print(pepa[3])

print(sys.getrefcount(pepa))

