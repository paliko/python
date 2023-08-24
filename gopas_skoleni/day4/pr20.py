#nechci ukladat jen radky ale nake slozity data

import pickle #pro serializaci deserializci dat (pythonovy datovy struktury)
import json

data = [1,2,3,1.2,2.3, "ahoj",(1,2,3),{1,2,3}]

# with open("data.pickle",mode="wb") as s: #pro zapis
with open("data.pickle",mode="rb") as s:
    # pickle.dump(data,s) # na prvni pohled tam nic neuvidime, museli by jsme mrknout na dokumentaci

    print(pickle.load(s)) #kdyz chci data nacist, zmenit mode na "rb"

print(pickle.loads(pickle.dumps(data))) #nemusim ukladat do filu muzu rovnou prevest


data = [1,2,3,1.2,2.3, "ahoj",(1,2,3),(1,2,3)]
# with open("data.json",mode="w") as s:
with open("data.json",mode="r") as s:
    # json.dump(data,s)
    print(json.load(s))