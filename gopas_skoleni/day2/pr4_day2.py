import sys
from typing import Any

class Clovek:

    citac =1
    
    def __init__(self, jmeno:str="", vek:int=0): 
        self.jmeno = jmeno
        self.vek = vek
        self.id = self.__class__.citac
        self.__class__.citac +=1 


    @staticmethod
    def metoda1():
        pass

    @classmethod
    def metoda2(cls):
         pass
        

    #kdyz budu chti pracovat s objektem jako retezcem
    def __str__(self): 
        return self.jmeno
    
    def __add__(self,other):
        if (hasattr(other,"vek")):
             return self.vek + other.vek
        else:
             return self.vek + other
        
        # try:
        #      return self.vek + other.vek
        # except AttributeError:
        #      return self.vek + other
        
        # if (isinstance(other,Clovek)):
        #     return self.vek + other.vek
        # if (isinstance(other,int)):
        #      return self.vek + other
        
    def __radd__(self,other):
         return self.__add__(other)
    
   
    
        
    
    
    
    def __lt__(self,other):
        return self.vek<other.vek
    
    def __getitem__(self,item): #kdyz chceme iterova, kdyz chcem iterator pr6
        return self.jmeno[item]
    
    def __setitem__(self,key, value):
         print(f"{key}: {value}")   #f formatovaci retezec jinak by vypsalo "{key}: {value}"

    def __call__(self,p): #muzu zkusit ze to vrati sinus
         import math
         return math.sin(p)
    
    def __del__(self): #jen vytiskne vymazani objektu, stara se o to sam sytem automaticky
                        # normalne se implementovat nebude, nestarame se vetsinou o ukonceni objektu
         print(f"KONEC CLOVEKA: {self.jmeno}")

    # def __getattr__(self, item):
    #     print(f"CHCETE PO ME aatribut : {item}")

    def tiskni(self): #nechci aby mela parametry, potrebuju odkazat na parametry pepy, ktere jeste nemam
            #kazda metoda v pythonu musi mit aspon jeden parametr - self, nemusi se to jmenovat self ale je to zvykem
        print(f"Jmeno : {self.jmeno}, vek : {self.vek}")



class Student(Clovek):
    def __init__(self,jmeno="",vek=0,skola=""):
        super().__init__(jmeno,vek) #zavolam rodicovsky init
        self.skola = skola
        self.__prijmeni = "Novak"

    def tiskni(self):
         print(f"Jmeno : {self.jmeno}, vek : {self.vek}, skola : {self.skola}")


#pepa = Clovek() #vytvarim instance, zavolam jakobych zavolal funkci 
#nemusim mit, kdyz jsem pridal parametry do init
# pepa.jmeno = "Josef" #instancni promena, pepa ma svoji, lojza ma svoji
# pepa.vek = 10

adam = Student("Adam",15,"ZS")
adam.tiskni()

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

print("pepa.a: ")
# a = pepa.a # __getattr__

pepa[3]="neco" #set item
print(pepa[3])

#kdyz chci ziskat vek od pepy
print(pepa.vek)
print(getattr(pepa,"vek")) #vyhoda kdyz mam ten vek ve stringu

print("pepa +10",pepa+10)
print("10 + pepa",10 + pepa) #__radd__

print(sys.getrefcount(pepa))

print(dir(adam))
print(adam.__prijmeni) #koukni na priklad pr9

exit()
