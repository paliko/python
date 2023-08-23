


class Posloupnost:
    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.i=-1
        return self

    def __next__(self):
        if (self.i<self.max-1):
            self.i += 1
            return self.i
        else:
            raise StopIteration
        

for p in Posloupnost(5):
    print(p)

print(Posloupnost(10)) #neudela nic
# ale muzu zkusit pretypovat na list
print(list(Posloupnost(10)))