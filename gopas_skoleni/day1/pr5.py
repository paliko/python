
class Mocnina:
    def __init__(self,exponent):
        self.exponent = exponent
    def __call__(self,zaklad):
        return zaklad ** self.exponent
    
mocnina2 = Mocnina(2)
mocnina3 = Mocnina(3)

print(mocnina2(2))
print(mocnina3(2))