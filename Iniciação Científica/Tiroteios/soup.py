import requests
from bs4 import BeautifulSoup

dadosDesnecessarios = ["Mortos", "Civis", "Policiais", "Feridos", "Operação Policial", "Fonte", "Usuário"]
nomeArq = "dadosFogoCruzado.csv"
bd = open(nomeArq, "w")
bd.write(
    "LOCAL DO TIROTEIO,DATA DO TIROTEIO,HORÁRIO DO TIROTEIO,MORTES?,CIVIS MORTOS,POLICIAIS MORTOS,FERIDOS?,CIVIS FERIDOS,POLICIAIS FERIDOS,OPERAÇÃO POLICIAL?\n")
bd.close()
for i in range(1, 1000):
    try:
        r = requests.get("http://fogocruzado.org.br/tiroteio/" + str(i) + "/", auth=('user', 'pass'))
        teste = BeautifulSoup(r.text, "html.parser")

        valor = teste.find_all("div", class_="wpb_text_column wpb_content_element ")

        dados = ""
        for val in valor:
            x = val.get_text().strip().replace(",", "|")
            if x not in dadosDesnecessarios:
                dados += x + ","
        if dados != "":
            dados = dados.strip(",") + "\n"
            bd = open(nomeArq, "a")
            bd.write(dados)
            bd.close()
    except:
        continue