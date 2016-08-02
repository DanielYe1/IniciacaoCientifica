import folium

map = folium.Map(location=[-22.862491371699999, -43.376356546200000], zoom_start=10,
                 tiles='Stamen Toner')
for i in range(4,13):
    string = "latlong"+str(i)+".csv"
    save = "osm"+str(i)+".html"
    bd = open(string, "r")
    for linha in bd:
        dados = linha.split(",")
        map.circle_marker(location=[dados[1], dados[2]], radius=60, popup=dados[0], line_color='#3186cc')
    bd.close()
    map.save(save)
