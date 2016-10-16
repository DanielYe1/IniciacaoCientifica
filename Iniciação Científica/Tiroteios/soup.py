import requests
import re
from bs4 import BeautifulSoup

dadosDesnecessarios = ["Mortos", "Civis", "Policiais", "Feridos", "Operação Policial", "Fonte", "Usuário", "Imprensa"]

nomeArq = "dadosFogoCruzado.csv"
with open(nomeArq, 'w', newline='') as csvfile:
    csvfile.write(
        "LOCAL DO TIROTEIO,DATA DO TIROTEIO,HORÁRIO DO TIROTEIO,MORTES?,CIVIS MORTOS,POLICIAIS MORTOS,FERIDOS?,CIVIS FERIDOS,POLICIAIS FERIDOS,OPERAÇÃO POLICIAL?,LATITUDE,LONGITUDE,INDEX\n")
for i in range(0, 3500):
    try:
        r = requests.get("http://fogocruzado.org.br/tiroteio/" + str(i) + "/", auth=('user', 'pass'))
        data = BeautifulSoup(r.text, "html.parser")

        valor = data.find_all("div", class_="wpb_text_column wpb_content_element ")

        dados = ""
        for val in valor:
            x = val.get_text().strip().replace(",", "|")
            if x not in dadosDesnecessarios:
                dados += x + ","

        location = re.findall('de_mapa_atual = (.*);', str(data))
        for x in location:
            dados += str(x) + ","

        if dados != "":
            dados = dados.strip(",") + "," + str(i) + "\n"
            bd = open(nomeArq, "a")
            bd.write(dados)
            bd.close()
    except:
        continue
