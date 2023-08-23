class Clovek():
    def __init__(self,jmeno=""):
        self.__jmeno = jmeno

    # def getJmeno(self):
    #     return self.__jmeno
    

    #misto toho muzu udelat: , tento dekorator nam umoznil ze muzu vytisknout jmeno, neco jako getter
    #property - diky ni verne zpristupnena promena
    @property
    def jmeno(self):
        return self.__jmeno


    @jmeno.setter
    def jmeno(self,jmeno):
        self.__jmeno = jmeno

pepa = Clovek("Josef")

pepa.jmeno  = "PEPA" #diky setteru

# print(pepa.getJmeno())
print(pepa.jmeno) #spojeno jmenem metody
