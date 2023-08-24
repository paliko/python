import multiprocessing, time


# vysl = []
# mutex = multiprocessing.Lock()

class Citac(multiprocessing.Process):
    def __init__(self,id):
        super().__init__()
        self.id=id
        self.deamon=False
    
    def run(self): #to co vytvari ten beh
        c=1
        while True:
            text = (f"Citac : {self.id} - {c}")
            print(text)
            c+=1
            time.sleep(1)


if (__name__=="__main__"):
    proces1 = Citac(1)
    proces2 = Citac(2)
    proces1.start()
    proces2.start()






