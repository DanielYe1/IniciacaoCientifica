""""
for i in range(1, 13):
    nome = "Casos_Notificados_Dengue_" + str(i).zfill(2) + "_2012.csv"
    nome2 = input()
    bd = open(nome, "r")
    bdA = open(nome2, "w")
    for line in bd:
        dados = line.split(",")
        bdA.write("{0},{1},{2}\n".format(dados[6].strip(), dados[57].strip(), dados[56].strip()))
    bd.close()
    bdA.close()

"""
for i in range(5):
    nome = "Casos_Notificados_Dengue_01_201" + str(i) + ".csv"
    nome2 = "casosJaneiro_201" + str(i)+".csv"
    bd = open(nome, "r")
    bdA = open(nome2, "w")
    for line in bd:
        dados = line.split(",")
        if (dados[33].strip() != ""):
            bdA.write(
                "{0},{1},{2},{3}\n".format(dados[6].strip(), dados[33].strip(), dados[57].strip(), dados[56].strip()))
    bd.close()
    bdA.close()
