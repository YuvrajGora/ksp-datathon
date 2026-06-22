from flask import Flask, render_template
import plotly.express as px
import plotly.utils
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
from crime_data import get_crime_trends, get_district_crimes, get_crime_types

app = Flask(__name__)

@app.route("/")
def home():
    # Crime trends line chart
    df_trends = get_crime_trends()
    fig_trends = px.line(df_trends, x="Month", 
                         y=["Theft", "Assault", "Fraud", "Robbery"],
                         title="Monthly Crime Trends 2024",
                         template="plotly_dark",
                         color_discrete_sequence=["#f85149", "#58a6ff", "#3fb950", "#d29922"])
    fig_trends.update_layout(paper_bgcolor="#161b22", plot_bgcolor="#161b22")
    chart_trends = json.dumps(fig_trends, cls=plotly.utils.PlotlyJSONEncoder)

    # District bar chart
    df_district = get_district_crimes()
    fig_district = px.bar(df_district, x="District", y="Total_Crimes",
                          title="Top 10 Districts by Crime Count",
                          template="plotly_dark",
                          color="Total_Crimes",
                          color_continuous_scale="Reds")
    fig_district.update_layout(paper_bgcolor="#161b22", plot_bgcolor="#161b22")
    chart_district = json.dumps(fig_district, cls=plotly.utils.PlotlyJSONEncoder)

    # Crime types pie chart
    df_types = get_crime_types()
    fig_types = px.pie(df_types, names="Crime_Type", values="Count",
                       title="Crime Distribution by Type",
                       template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Reds)
    fig_types.update_layout(paper_bgcolor="#161b22", plot_bgcolor="#161b22")
    chart_types = json.dumps(fig_types, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", 
                           chart_trends=chart_trends,
                           chart_district=chart_district,
                           chart_types=chart_types)

if __name__ == "__main__":
    app.run(debug=True)