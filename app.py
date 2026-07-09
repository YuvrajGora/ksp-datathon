from flask import Flask, render_template, request, jsonify
import json
import sys
import os

# Fix path FIRST before any imports
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
sys.path.insert(0, data_path)

# Now import data modules
from crime_data import get_crime_trends, get_district_crimes, get_crime_types
from map_generator import generate_crime_map

app = Flask(__name__)

@app.route("/")
def home():
    df_trends = get_crime_trends()
    months = df_trends["Month"].tolist()
    
    chart_trends = json.dumps({
        "data": [
            {"x": months, "y": df_trends["Theft"].tolist(),
             "type": "scatter", "mode": "lines", "name": "Theft",
             "line": {"color": "#f85149", "width": 2}},
            {"x": months, "y": df_trends["Assault"].tolist(),
             "type": "scatter", "mode": "lines", "name": "Assault",
             "line": {"color": "#58a6ff", "width": 2}},
            {"x": months, "y": df_trends["Fraud"].tolist(),
             "type": "scatter", "mode": "lines", "name": "Fraud",
             "line": {"color": "#3fb950", "width": 2}},
            {"x": months, "y": df_trends["Robbery"].tolist(),
             "type": "scatter", "mode": "lines", "name": "Robbery",
             "line": {"color": "#d29922", "width": 2}}
        ],
        "layout": {
            "title": "Monthly Crime Trends 2024",
            "paper_bgcolor": "#161b22",
            "plot_bgcolor": "#161b22",
            "font": {"color": "white"},
            "xaxis": {"title": "Month", "gridcolor": "#30363d"},
            "yaxis": {"title": "Count", "gridcolor": "#30363d"}
        }
    })

    df_district = get_district_crimes()
    chart_district = json.dumps({
        "data": [{
            "x": df_district["District"].tolist(),
            "y": df_district["Total_Crimes"].tolist(),
            "type": "bar",
            "marker": {"color": ["#ff0000", "#ff2200", "#ff4400", "#ff6600",
                                  "#ff8800", "#ffaa00", "#ffcc00", "#ff9900",
                                  "#ff7700", "#ff5500"]}
        }],
        "layout": {
            "title": "Top 10 Districts by Crime Count",
            "paper_bgcolor": "#161b22",
            "plot_bgcolor": "#161b22",
            "font": {"color": "white"},
            "xaxis": {"title": "District", "gridcolor": "#30363d"},
            "yaxis": {"title": "Total Crimes", "gridcolor": "#30363d"}
        }
    })

    df_types = get_crime_types()
    chart_types = json.dumps({
        "data": [{
            "labels": df_types["Crime_Type"].tolist(),
            "values": df_types["Count"].tolist(),
            "type": "pie",
            "marker": {"colors": ["#ff0000", "#ff3300", "#ff6600",
                                   "#ff9900", "#ffcc00", "#cc0000", "#990000"]}
        }],
        "layout": {
            "title": "Crime Distribution by Type",
            "paper_bgcolor": "#161b22",
            "plot_bgcolor": "#161b22",
            "font": {"color": "white"}
        }
    })

    return render_template("index.html",
                           chart_trends=chart_trends,
                           chart_district=chart_district,
                           chart_types=chart_types)

@app.route("/map")
def crime_map():
    try:
        generate_crime_map()
        return render_template("map.html")
    except Exception as e:
        return f"Map error: {str(e)}", 500

@app.route("/network")
def network():
    return render_template("network.html")

@app.route("/risk")
def risk():
    return render_template("risk.html")

@app.route("/filter")
def filter_page():
    return render_template("filter.html")

@app.route("/predict", methods=["POST"])
def predict():
    from crime_model import predict_risk
    data = request.json
    result = predict_risk(
        data["district"],
        int(data["month"]),
        data["time"],
        data["crime_type"]
    )
    return jsonify(result)

@app.route("/offenders")
def offenders():
    return render_template("offenders.html")

@app.route("/socio")
def socio():
    return render_template("socio.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)