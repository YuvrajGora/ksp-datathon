# 🚔 KSP Crime Analytics Dashboard
### AI-Powered Crime Intelligence Platform for Karnataka State Police

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![ML](https://img.shields.io/badge/ML-RandomForest-orange)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

> **KSP Datathon 2026 — Challenge 02**  
> Built by **Yuvraj Gora** | Team: **The Solo Rider**

---

## 🌐 Live Demo
**[https://ksp1-50043372326.development.catalystappsail.in](https://ksp1-50043372326.development.catalystappsail.in)**

---

## 📌 Problem Statement
The Karnataka State Police SCRB manages crime data from 1100+ police stations across Karnataka. Current systems rely on static dashboards and manual Excel-based reporting, making it impossible to detect patterns, predict risks, or visualize criminal networks in real time.

---

## 💡 Solution
A modern AI-powered crime analytics platform that transforms raw crime data into actionable intelligence through interactive visualizations, machine learning predictions, and network analysis.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Interactive Dashboard** | Real-time charts showing crime trends, district comparisons and type distribution, plus automated anomaly alerts |
| 🗺️ **Crime Hotspot Map** | Interactive Karnataka map with heatmap overlay and risk-colored district markers |
| 🕸️ **Criminal Network Analysis** | Node-based visualization of criminal associations and repeat offender connections |
| 🤖 **AI Risk Predictor** | Random Forest ML model predicting crime risk by district, time and crime type |
| 🔍 **Search & Filter** | Dynamic filtering by district, crime type, time period and risk level |
| 👤 **Repeat Offender Tracking** | Behavioral profiling and linked incident tracking for repeat offenders |
| 📈 **Socio-Economic Correlation** | Crime data correlated against socio-economic indicators |

---

## 🛠️ Tech Stack

**Backend**
- Python 3.13
- Flask 3.1
- Pandas & NumPy
- Scikit-learn (Random Forest Classifier)

**Frontend**
- HTML5 & CSS3
- Plotly.js (Interactive Charts)
- Folium (Map Visualization)

**Deployment**
- Zoho Catalyst AppSail (Live Hosting — Catalyst-Managed Python 3.13 Runtime)
- GitHub (Version Control)

---

## 📸 Screenshots

### Dashboard
> Interactive dark-themed dashboard with crime trend charts

### Crime Hotspot Map  
> Karnataka map with heatmap overlay showing crime concentration

### Criminal Network
> Node-based visualization of criminal associations

### AI Risk Predictor
> ML-powered real-time risk scoring

### Repeat Offender Tracking
> Behavioral profiling for tracked offenders across districts

### Socio-Economic Correlation
> Crime patterns correlated against socio-economic indicators

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/YuvrajGora/ksp-datathon.git
cd ksp-datathon/ksp-datathon

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### Access
Open your browser and go to `http://localhost:9000`

---

## 📁 Project Structure
```
ksp-datathon/
├── app.py                  # Flask application & routes
├── requirements.txt         # Python dependencies
├── runtime.txt              # Python version pin
├── app-config.json          # Catalyst AppSail runtime configuration
├── catalyst.json            # Catalyst project/resource linkage
├── vendor/                  # Bundled Linux-compatible dependencies (Catalyst deployment)
├── data/
│   ├── crime_data.py         # Karnataka crime dataset
│   ├── crime_model.py        # ML Random Forest model
│   └── map_generator.py      # Folium map generator
└── templates/
    ├── index.html            # Main dashboard
    ├── map.html              # Crime hotspot map
    ├── network.html          # Criminal network viz
    ├── risk.html             # AI risk scoring
    ├── filter.html           # Search & filter
    ├── offenders.html        # Repeat offender tracking
    └── socio.html            # Socio-economic correlation
```

---

## 🤖 ML Model Details
- **Algorithm:** Random Forest Classifier
- **Features:** District, Month, Time of Day, Crime Type
- **Output:** Risk Level (Critical/High/Medium/Low) + Confidence Score

---

## 📊 Key Insights
- **Bengaluru Urban** accounts for ~25% of all Karnataka crimes
- **Theft** is the most common crime across all districts
- **Night time (10PM-6AM)** shows higher crime risk
- **December** consistently shows highest crime rates (festival season)

---

## 🎯 Impact
- Replaces manual Excel reporting with real-time AI analytics
- Enables proactive policing through predictive risk scoring
- Visualizes hidden criminal networks impossible to spot manually
- Covers all 30 Karnataka districts with drill-down capability

---

## 👤 Author
**Yuvraj Gora**  
1st Year Student | KSP Datathon 2026  
Team: The Solo Rider

---

*Built with ❤️ for Karnataka State Police Datathon 2026*
