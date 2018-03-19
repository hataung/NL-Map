import folium
map = folium.Map(location=[52.1326, 5.29131], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="NL Map")
fg.add_child(folium.Marker(location=[52.3702, 4.8952], popup="Hello This is Amsterdam!", icon=folium.Icon(color='orange')))
fg.add_child(folium.Marker(location=[50.8514, 5.6910], popup="Hello This is Maastricht!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("NL_Map.html")
