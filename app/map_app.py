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
    [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip=tooltip).add_to(map)
    return map._repr_html_()