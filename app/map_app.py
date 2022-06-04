from flask import Blueprint, render_template
import folium

map_app = Blueprint('map_app', __name__,static_folder="static", template_folder='templates')
@map_app.route("/map")
def open_street_map():
    map = folium.Map(
        location=[21.3891, -39.8579],
        zoom_start=2
    )
    return map._repr_html_()

@map_app.route("/map-marker")
def map_marker():
    map = folium.Map(
        location=[21.3891, -39.8579],
        zoom_start=2
    )
    return map._repr_html_()