import pandas as pd

def get_crime_trends():
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Theft": [320, 290, 310, 280, 350, 400, 380, 360, 330, 290, 310, 420],
        "Assault": [180, 160, 170, 150, 190, 210, 200, 185, 175, 160, 170, 220],
        "Fraud": [90, 85, 95, 88, 102, 115, 108, 98, 92, 85, 95, 125],
        "Robbery": [45, 40, 42, 38, 50, 58, 54, 48, 44, 40, 43, 62]
    }
    return pd.DataFrame(data)

def get_district_crimes():
    data = {
        "District": ["Bengaluru Urban", "Mysuru", "Tumkur", "Belagavi",
                     "Mangaluru", "Kalaburagi", "Davanagere", "Ballari",
                     "Vijayapura", "Shivamogga"],
        "Total_Crimes": [3200, 890, 650, 720, 580, 490, 410, 380, 350, 320]
    }
    return pd.DataFrame(data)

def get_crime_types():
    data = {
        "Crime_Type": ["Theft", "Assault", "Fraud", "Robbery",
                       "Cybercrime", "Domestic Violence", "Drug Offences"],
        "Count": [4200, 2100, 1800, 650, 890, 1200, 430]
    }
    return pd.DataFrame(data)

def get_district_coordinates():
    data = {
        "District": ["Bengaluru Urban", "Mysuru", "Tumkur", "Belagavi",
                     "Mangaluru", "Kalaburagi", "Davanagere", "Ballari",
                     "Vijayapura", "Shivamogga", "Hubballi", "Bidar",
                     "Raichur", "Koppal", "Gadag", "Dharwad",
                     "Uttara Kannada", "Haveri", "Bagalkot", "Chitradurga",
                     "Chikkamagaluru", "Hassan", "Kodagu", "Mandya",
                     "Chamarajanagar", "Bengaluru Rural", "Ramanagara",
                     "Chikkaballapura", "Kolar", "Yadgir"],
        "Lat": [12.97, 12.29, 13.34, 15.85, 12.91, 17.33, 14.46, 15.15,
                16.83, 13.93, 15.36, 17.91, 16.21, 15.35, 15.43, 15.46,
                14.80, 14.79, 16.18, 14.23, 13.32, 13.00, 12.42, 12.52,
                11.94, 13.16, 12.72, 13.43, 13.13, 16.76],
        "Lon": [77.59, 76.63, 77.10, 74.49, 74.85, 76.82, 75.92, 76.94,
                75.72, 75.56, 75.12, 77.52, 77.36, 76.15, 75.63, 75.01,
                74.49, 75.44, 75.70, 76.40, 75.77, 76.10, 75.74, 76.90,
                77.17, 77.50, 77.28, 77.73, 78.13, 77.38],
        "Total_Crimes": [3200, 890, 650, 720, 580, 490, 410, 380,
                         350, 320, 440, 290, 310, 270, 250, 360,
                         280, 240, 300, 330, 290, 310, 180, 420,
                         260, 380, 340, 290, 310, 220],
        "Risk_Level": ["Very High", "High", "Medium", "High", "Medium", "Medium",
                       "Low", "Low", "Medium", "Low", "Medium", "Low", "Low",
                       "Low", "Low", "Medium", "Low", "Low", "Low", "Medium",
                       "Low", "Medium", "Low", "Medium", "Low", "Medium",
                       "Medium", "Low", "Medium", "Low"]
    }
    return pd.DataFrame(data)