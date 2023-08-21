from typing import List, Dict, Union
def soucet(a:int,b:int) -> int: #chci aby ty parametry byly int
    return a+b

v = soucet(2.0,3)
print(v)

a:int = 0

#timto komentarem rikam ze chci vytvorit list integeru
l = [] # type: List[int]

l.append(1)
l.append(1.2)
print(l)