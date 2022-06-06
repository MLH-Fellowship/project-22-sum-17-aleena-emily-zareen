from flask import Blueprint, render_template
import folium

map_app = Blueprint('map_app', __name__,static_folder="static", template_folder='templates')
@map_app.route("/aleena-map")
def aleenamap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )
    return map._repr_html_()
@map_app.route("/emily-map")
def emilymap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )    
    return map._repr_html_()

@map_app.route("/zareen-map")
def zareenmap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )
    tooltip = "Click me!"
    folium.Marker(
    [48.8633611,2.3551446], popup="<i>Paris, France</i>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [28.520723, 84.038404], popup="<b>Himalayas, Nepal</b>", tooltip=tooltip).add_to(map)
    return map._repr_html_()