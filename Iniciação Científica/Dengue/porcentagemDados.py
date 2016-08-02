for i in range(5):
    nome = "D:/Daniel/PycharmProjects/test/Iniciação Científica/dadosTotal/Dengue_201" + str(
        i) + "/Casos_Notificados_Dengue_02_201" + str(
        i) + ".csv"

    bd = open(nome, "r")
    linha1 = True
    linha2 = False
    vetor = []
    count = 0
    dado = "ID_OCUPA_N"
    for linha in bd:
        if linha1:
            linha1 = False
            linha2 = True
            continue
        elif linha2:
            dados = linha.split(",")
            if dados.count(dado) != 1:
                break
            k = dados.index(dado)
            linha2 = False
            continue
        else:
            dados = linha.split(",")
            if dados[k] != " ":
                count += 1
    print(count)
    bd.close()
