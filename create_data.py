import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

data = {
    'Make': [], 'Model': [], 'Year': [], 'Engine Size': [], 
    'Mileage': [], 'Fuel Type': [], 'Transmission': [], 'Price': []
}

# 50 vehicles: 10 brands * 5 models each
cars_fleet = {
    'Maruti Suzuki': [
        ('Swift', [1.2], ['Petrol'], ['Manual', 'Automatic'], 600000, 950000),
        ('Baleno', [1.2], ['Petrol'], ['Manual', 'Automatic'], 660000, 990000),
        ('Brezza', [1.5], ['Petrol'], ['Manual', 'Automatic'], 830000, 1410000),
        ('Ertiga', [1.5], ['Petrol', 'CNG'], ['Manual', 'Automatic'], 860000, 1300000),
        ('Dzire', [1.2], ['Petrol', 'CNG'], ['Manual', 'Automatic'], 650000, 930000)
    ],
    'Hyundai': [
        ('Creta', [1.5], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1100000, 2000000),
        ('i20', [1.2], ['Petrol'], ['Manual', 'Automatic'], 740000, 1160000),
        ('Verna', [1.5], ['Petrol'], ['Manual', 'Automatic'], 1100000, 1740000),
        ('Venue', [1.0, 1.2], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 790000, 1340000),
        ('Alcazar', [1.5, 2.0], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1670000, 2120000)
    ],
    'Tata': [
        ('Nexon', [1.2, 1.5], ['Petrol', 'Diesel', 'Electric'], ['Manual', 'Automatic'], 810000, 1550000),
        ('Harrier', [2.0], ['Diesel'], ['Manual', 'Automatic'], 1540000, 2640000),
        ('Safari', [2.0], ['Diesel'], ['Manual', 'Automatic'], 1610000, 2730000),
        ('Altroz', [1.2, 1.5], ['Petrol', 'Diesel', 'CNG'], ['Manual', 'Automatic'], 660000, 1070000),
        ('Tiago', [1.2], ['Petrol', 'CNG', 'Electric'], ['Manual', 'Automatic'], 560000, 820000)
    ],
    'Mahindra': [
        ('Thar', [1.5, 2.0, 2.2], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1130000, 1760000),
        ('XUV700', [2.0, 2.2], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1390000, 2690000),
        ('Scorpio-N', [2.0, 2.2], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1360000, 2450000),
        ('Bolero', [1.5], ['Diesel'], ['Manual'], 990000, 1090000),
        ('XUV300', [1.2, 1.5], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 790000, 1470000)
    ],
    'Honda': [
        ('City', [1.5], ['Petrol', 'Hybrid'], ['Manual', 'Automatic'], 1180000, 1630000),
        ('Amaze', [1.2], ['Petrol'], ['Manual', 'Automatic'], 720000, 990000),
        ('Elevate', [1.5], ['Petrol'], ['Manual', 'Automatic'], 1160000, 1650000),
        ('Jazz', [1.2], ['Petrol'], ['Manual', 'Automatic'], 800000, 1030000),
        ('Civic', [1.8, 2.0], ['Petrol'], ['Automatic'], 1800000, 2200000)
    ],
    'Kia': [
        ('Seltos', [1.5], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1090000, 2030000),
        ('Sonet', [1.0, 1.2, 1.5], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 790000, 1570000),
        ('Carens', [1.4, 1.5], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1040000, 1940000),
        ('Carnival', [2.2], ['Diesel'], ['Automatic'], 3100000, 3500000),
        ('EV6', [0.0], ['Electric'], ['Automatic'], 6000000, 6500000)
    ],
    'Toyota': [
        ('Fortuner', [2.7, 2.8], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 3340000, 5140000),
        ('Innova Hycross', [2.0], ['Petrol', 'Hybrid'], ['Automatic'], 1970000, 3090000),
        ('Glanza', [1.2], ['Petrol', 'CNG'], ['Manual', 'Automatic'], 680000, 1000000),
        ('Urban Cruiser', [1.5], ['Petrol'], ['Manual', 'Automatic'], 1110000, 1580000),
        ('Camry', [2.5], ['Hybrid'], ['Automatic'], 4600000, 4800000)
    ],
    'MG': [
        ('Hector', [1.5, 2.0], ['Petrol', 'Diesel'], ['Manual', 'Automatic'], 1400000, 2200000),
        ('Astor', [1.3, 1.5], ['Petrol'], ['Manual', 'Automatic'], 990000, 1800000),
        ('ZS EV', [0.0], ['Electric'], ['Automatic'], 1890000, 2540000),
        ('Comet EV', [0.0], ['Electric'], ['Automatic'], 690000, 960000),
        ('Gloster', [2.0], ['Diesel'], ['Automatic'], 3800000, 4300000)
    ],
    'Skoda': [
        ('Kushaq', [1.0, 1.5], ['Petrol'], ['Manual', 'Automatic'], 1080000, 2000000),
        ('Slavia', [1.0, 1.5], ['Petrol'], ['Manual', 'Automatic'], 1060000, 1860000),
        ('Superb', [2.0], ['Petrol'], ['Automatic'], 3400000, 3800000),
        ('Octavia', [2.0], ['Petrol'], ['Automatic'], 2700000, 3000000),
        ('Kodiaq', [2.0], ['Petrol'], ['Automatic'], 3800000, 4100000)
    ],
    'Volkswagen': [
        ('Taigun', [1.0, 1.5], ['Petrol'], ['Manual', 'Automatic'], 1160000, 1970000),
        ('Virtus', [1.0, 1.5], ['Petrol'], ['Manual', 'Automatic'], 1140000, 1910000),
        ('Tiguan', [2.0], ['Petrol'], ['Automatic'], 3500000, 3700000),
        ('Polo', [1.0], ['Petrol'], ['Manual', 'Automatic'], 650000, 1050000),
        ('Vento', [1.0], ['Petrol'], ['Manual', 'Automatic'], 1000000, 1400000)
    ]
}

makes = list(cars_fleet.keys())

for _ in range(5000):
    make = np.random.choice(makes)
    car_list = cars_fleet[make]
    car_tuple = car_list[np.random.randint(0, len(car_list))]
    
    model, engine_options, fuels, transmissions, min_price, max_price = car_tuple
    
    year = np.random.randint(2012, 2025)
    engine = np.random.choice(engine_options)
    fuel = np.random.choice(fuels)
    transmission = np.random.choice(transmissions)
    mileage = np.random.randint(2000, 140000)
    
    # Calculate synthetic price with Random-Forest-friendly logic
    base_price = np.random.uniform(min_price, max_price)
    age_depreciation = (2025 - year) * 0.06 * base_price
    mileage_depreciation = mileage * 1.8 
    
    final_price = max(base_price - age_depreciation - mileage_depreciation, base_price * 0.15)
    
    data['Make'].append(make)
    data['Model'].append(model)
    data['Year'].append(year)
    data['Engine Size'].append(engine)
    data['Mileage'].append(mileage)
    data['Fuel Type'].append(fuel)
    data['Transmission'].append(transmission)
    data['Price'].append(final_price)

df = pd.DataFrame(data)
df.to_csv('Car_Price_Prediction.csv', index=False, encoding='utf-16')
print(f"Dataset generated with {len(df)} entries and 50 unique car models.")
