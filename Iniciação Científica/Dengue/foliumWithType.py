import folium

map = folium.Map(location=[-22.862491371699999, -43.376356546200000], zoom_start=10,
                 tiles='Stamen Toner')
string = "teste1.csv"
save = input()
bd = open(string, "r")
for linha in bd:
    dados = linha.split(",")
    if dados[1] == '1':
        map.circle_marker(location=[dados[2], dados[3]], radius=90, popup=dados[0], line_color='blue')
    elif dados[1] == '2':
        map.circle_marker(location=[dados[2], dados[3]], radius=90, popup=dados[0], line_color='green')
    elif dados[1] == '3':
        map.circle_marker(location=[dados[2], dados[3]], radius=90, popup=dados[0], line_color='yellow')
    elif dados[1] == '4':
        map.circle_marker(location=[dados[2], dados[3]], radius=90, popup=dados[0], line_color='red')
bd.close()
map.save(save)
