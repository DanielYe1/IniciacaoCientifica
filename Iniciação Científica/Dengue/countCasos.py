for i in range(1, 13):
    nome = "D:/Daniel/PycharmProjects/test/Iniciação Científica/dadosTotal/Dengue_2014/Casos_Notificados_Dengue_" + str(
        i).zfill(2) + "_2014.csv"
    count = 0

    bd = open(nome, "r")
    for linha in bd:
        count += 1
    print(str(count-2))
    bd.close()
