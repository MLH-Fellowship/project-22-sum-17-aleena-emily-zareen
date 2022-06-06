from flask import Blueprint, render_template
import folium

map_app = Blueprint('map_app', __name__,static_folder="static", template_folder='templates')
@map_app.route("/aleena-map")
def aleenamap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )
    tooltip = "Click me!"
    folium.Marker(
    [34.052235,-118.243683], popup="<b>Los Angeles, California</b>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [43.534321, -80.243683], popup="<b>Niagara Falls, Canada</b>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [11.9344, -84.9560], popup="<b>Granada, Nicaragua</b>", tooltip=tooltip).add_to(map)
    return map._repr_html_()

@map_app.route("/emily-map")
def emilymap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )    
    tooltip = "Click me!"
    folium.Marker(
    [52.509422,13.408891], popup="<b>Berlin, Germany</b>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [46.406252, -63.351648], popup="<b>New Glasgow, Canada</b>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [49.271674, -123.103113], popup="<b>Vancouver, Canada</b>", tooltip=tooltip).add_to(map)
    return map._repr_html_()

@map_app.route("/zareen-map")
def zareenmap():
    map = folium.Map(
        location=[21.018254, 8.457681],
        zoom_start=2
    )
    tooltip = "Click me!"
    folium.Marker(
    [48.8633611,2.3551446], popup="<b>Paris, France</b>", tooltip=tooltip).add_to(map)
    folium.Marker(
    [28.520723, 84.038404], popup="<b>Himalayas, Nepal</b>", tooltip=tooltip).add_to(map)
    return map._repr_html_()
