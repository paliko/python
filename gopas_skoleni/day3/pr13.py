
import math, itertools

#pole prvky spocita pro sude prvky sinus
v=[]

for i in range(1000):
    if (i%2==0):
        v.append(math.sin(i))


#dalo by se nahradit
v = [math.sin(i) for i in range(1000) if i%2==0] # tohle je jeden krok - atomicka operace, uvnitr je sice nakej cyklus ale ten ja nevidim
print(len(v))


v = (math.sin(i) for i in range(1000) if i%2==0) # vymenim zavorky a vytvorim n tici - iterovatelny
#muzu prevest na seznam
print(list(v))


def soucet(a,b):
    return a+b

c1 = [1,2,3,4,5]
c2 = [10,213,43,34,34]

v = map(soucet,c1,c2) #prvni funkce, pak prvky
print(list(v))
print(c1+c2)

v = map(lambda a,b:a+b, c1,c2)
print(tuple(v))

# v = filter(lambda a:not a%2 AND a!=4,c1) #musi mit jeden parametr, fitruje tu funkci a vraci prvky
#  pro ktere je pravdiva
print(tuple(v))


v = zip(c1,c2)
print(tuple(v))


#conditional expression
a=1
b=2

max = a if a>b else b