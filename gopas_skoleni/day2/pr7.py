def fce(a,b,c=1): #defaultni parametry muusi byt na konci
    return a+b+c

def fce2(*args,**kwargs): #jedno jak se jmenujou, dulezite jeden ma jednu hvezdicku, druhej dve
                            #keyword argumnt proto kw
                            # * predany vsechny pozicni argumenty
                            # ** vsechny
    print(args)
    print(kwargs)

print(fce(1,2,3))
fce(1,2)

fce(b=1,a=1) #vyhoda ze muzeme predat parametry pojmenovane, 
            #kdyz budu mit deset optional a muzu predat par jen ty ktere chci a nevypisovat vsechny

print("ahoj",end="\n\n")        

fce2(1,2,3,x=10,y=20)

#muzu udelat tohle: parametry nepredam jednotlive ale v sekvencich
fce(*(1,2,3))
fce2(*(1,2,3),**{"x"=10,"y"=20})    

#mohl bych prepsat studenta pomoci kwargs, mam hodne parametru a nechci je prepisovat, tak je muzu zvolat timhle

