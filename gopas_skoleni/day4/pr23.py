import shelve

with shelve.open("data.shelve") as sh:
    # sh["pepa"] = ("Josef","Novak",123)
    # sh["policei"] = 158
    # print(sh["pepa"])
    # print(sh["policei"])

    # for i in range(5000):
    #     sh[f"polozka{i}"] = (1,2,3)

    print(sh["polozka10"])
    print(sh["polozka1058"])