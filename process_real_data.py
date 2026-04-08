import pandas as pd
import io
import os

# Path to the raw data we fetched
RAW_DATA_PATH = r"C:\Users\omchu\.gemini\antigravity\brain\a42b4bfb-10fc-4f81-9be6-251d5a7db80e\.system_generated\steps\504\content.md"

with open(RAW_DATA_PATH, 'r') as f:
    lines = f.readlines()

# Skip the first 4 lines (Source, metadata)
csv_lines = [line for line in lines[4:] if ',' in line]
raw_csv_str = "".join(csv_lines)


# Dictionary to map real Car_Name to our (Make, Model)
# We'll augment the raw data with these mappings
mappings = {
    'ritz': ('Maruti Suzuki', 'Ritz'),
    'sx4': ('Maruti Suzuki', 'SX4'),
    'ciaz': ('Maruti Suzuki', 'Ciaz'),
    'wagon r': ('Maruti Suzuki', 'Wagon R'),
    'swift': ('Maruti Suzuki', 'Swift'),
    'vitara brezza': ('Maruti Suzuki', 'Brezza'),
    's cross': ('Maruti Suzuki', 'S Cross'),
    'alto 800': ('Maruti Suzuki', 'Alto 800'),
    'ertiga': ('Maruti Suzuki', 'Ertiga'),
    'dzire': ('Maruti Suzuki', 'Dzire'),
    'ignis': ('Maruti Suzuki', 'Ignis'),
    'baleno': ('Maruti Suzuki', 'Baleno'),
    'omni': ('Maruti Suzuki', 'Omni'),
    'fortuner': ('Toyota', 'Fortuner'),
    'innova': ('Toyota', 'Innova'),
    'corolla altis': ('Toyota', 'Corolla Altis'),
    'etios cross': ('Toyota', 'Etios Cross'),
    'etios g': ('Toyota', 'Etios'),
    'etios liva': ('Toyota', 'Etios Liva'),
    'camry': ('Toyota', 'Camry'),
    'land cruiser': ('Toyota', 'Land Cruiser'),
    'i20': ('Hyundai', 'i20'),
    'grand i10': ('Hyundai', 'Grand i10'),
    'i10': ('Hyundai', 'i10'),
    'eon': ('Hyundai', 'Eon'),
    'xcent': ('Hyundai', 'Xcent'),
    'elantra': ('Hyundai', 'Elantra'),
    'creta': ('Hyundai', 'Creta'),
    'verna': ('Hyundai', 'Verna'),
    'city': ('Honda', 'City'),
    'brio': ('Honda', 'Brio'),
    'amaze': ('Honda', 'Amaze'),
    'jazz': ('Honda', 'Jazz')
}

import io
df_real = pd.read_csv(io.StringIO(raw_csv_str))

# Map to new structure
processed_data = []
cities_metro = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
cities_tier2 = ['Ahmedabad', 'Pune', 'Jaipur', 'Lucknow', 'Kochi']

for index, row in df_real.iterrows():
    name = row['Car_Name'].lower()
    if name in mappings:
        make, model = mappings[name]
        
        # Determine Owner Type
        owner_val = int(row['Owner'])
        owner_type = "First Owner" if owner_val == 0 else "Second Owner" if owner_val == 1 else "Third Owner"
        
        # Determine Location (Dealers are more likely in Metros)
        if row['Seller_Type'] == 'Dealer':
            location = cities_metro[index % len(cities_metro)]
        else:
            location = cities_tier2[index % len(cities_tier2)]

        processed_data.append({
            'Make': make,            'Model': model,
            'Year': row['Year'],
            'Engine Size': 1.2 if 'i10' in name or 'swift' in name else 1.5,
            'Mileage': row['Kms_Driven'],
            'Fuel Type': row['Fuel_Type'],
            'Transmission': row['Transmission'],
            'Owner': owner_type,
            'Location': location,
            'Price': row['Selling_Price'] * 100000 
        })

df_final = pd.DataFrame(processed_data)
df_final.to_csv('Car_Price_Prediction_Real.csv', index=False, encoding='utf-8')
print("Successfully processed real dataset with", len(df_final), "records and NEW features (Owner, Location).")
