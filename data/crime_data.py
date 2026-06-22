# crime_data.py — Sample Karnataka Crime Data

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