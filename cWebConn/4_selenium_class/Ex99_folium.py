import folium

# [1]
map_temp = folium.Map(location=[37.576475086141166, 126.97688517070613],
                      zoom_start=17)  # zoom_start -> 16 ~ 19 사이
folium.Marker(location=[37.576475086141166, 126.97688517070613], popup='광화문',
              icon=folium.Icon(color='red', icon='info_sign')).add_to(map_temp)

folium.CircleMarker(location=[37.576475086141166, 126.97688517070613], popup='광화문',
                    radius=100, color='yellow', fill_color='AABB22') .add_to(map_temp)
map_temp.save('./map5.html')
