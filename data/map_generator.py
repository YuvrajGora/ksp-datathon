import folium
from folium.plugins import HeatMap
import sys
import os
sys.path.append(os.path.dirname(__file__))
from crime_data import get_district_coordinates

def generate_crime_map():
    df = get_district_coordinates()
    
    # Create base map centered on Karnataka
    m = folium.Map(
        location=[15.3173, 75.7139],
        zoom_start=7,
        tiles="CartoDB dark_matter"
    )

    # Color based on risk level
    def get_color(risk):
        if risk == "Very High": return "#ff0000"
        elif risk == "High": return "#ff6600"
        elif risk == "Medium": return "#ffaa00"
        else: return "#00cc44"

    # Add circle markers for each district
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["Lat"], row["Lon"]],
            radius=row["Total_Crimes"] / 100,
            color=get_color(row["Risk_Level"]),
            fill=True,
            fill_color=get_color(row["Risk_Level"]),
            fill_opacity=0.7,
            popup=folium.Popup(
                f"""
                <div style='font-family:Arial; min-width:150px'>
                    <b style='font-size:14px'>{row['District']}</b><br>
                    <hr style='margin:5px 0'>
                    🚨 Total Crimes: <b>{row['Total_Crimes']}</b><br>
                    ⚠️ Risk Level: <b>{row['Risk_Level']}</b>
                </div>
                """,
                max_width=200
            ),
            tooltip=f"{row['District']} — {row['Total_Crimes']} crimes"
        ).add_to(m)

    # Add heatmap layer
    heat_data = [[row["Lat"], row["Lon"], row["Total_Crimes"]] 
                 for _, row in df.iterrows()]
    HeatMap(heat_data, radius=40, blur=25, 
            gradient={"0.4": "blue", "0.6": "lime", 
                      "0.8": "orange", "1": "red"}).add_to(m)

    # Add legend
    legend_html = """
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
                background: rgba(0,0,0,0.8); padding: 15px; border-radius: 10px;
                color: white; font-family: Arial; font-size: 13px;">
        <b>🗺️ Risk Level</b><br>
        <span style="color:#ff0000">●</span> Very High<br>
        <span style="color:#ff6600">●</span> High<br>
        <span style="color:#ffaa00">●</span> Medium<br>
        <span style="color:#00cc44">●</span> Low
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Add navbar
    navbar_html = """
    <div style="position:fixed;top:0;left:0;right:0;z-index:9999;background:#161b22;
                padding:15px 30px;display:flex;align-items:center;gap:15px;
                border-bottom:2px solid #f85149;">
        <h1 style="font-size:20px;color:#f85149;margin:0;">🚔 KSP Crime Analytics</h1>
        <span style="color:#8b949e;font-size:13px;">Karnataka State Police — SCRB Intelligence Dashboard</span>
        <div style="margin-left:auto;display:flex;gap:15px;">
            <a href="/" style="color:#8b949e;text-decoration:none;">📊 Dashboard</a>
            <a href="/map" style="color:#f85149;text-decoration:none;">🗺️ Crime Map</a>
            <a href="/network" style="color:#8b949e;text-decoration:none;">🕸️ Network</a>
            <a href="/risk" style="color:#8b949e;text-decoration:none;">🤖 AI Risk</a>
        </div>
    </div>
    <div style="height:60px;"></div>
    """
    m.get_root().html.add_child(folium.Element(navbar_html))

    # Save to dynamic writeable space
    map_path = "/tmp/map.html"
    m.save(map_path)
    return map_path