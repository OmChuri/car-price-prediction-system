# 🚗 Car Price Prediction System

An end-to-end Machine Learning project that predicts car prices based on features such as brand, year, mileage, fuel type, and transmission. The project is deployed as a Flask web application with a modern UI for real-time predictions.

---

## 🔥 Features

* 🤖 **Machine Learning Model**
  Built using **Random Forest Regression** to capture complex relationships between car features.

* 📊 **High Accuracy**

  * **R² Score**: ~97.5%
  * **MAE**: ~₹1.06 Lakh
  * **RMSE**: ~₹1.48 Lakh

* 🌐 **Flask Web Application**
  Users can input vehicle details and get instant price predictions.

* 🎨 **Modern UI Design**
  Clean and responsive interface with glassmorphism styling.

* 📁 **Multiple Datasets**

  * Synthetic dataset
  * Real-world dataset preprocessing included

---

## 📸 Screenshots

### 🔹 Input Form

<img width="1893" height="901" alt="input" src="https://github.com/user-attachments/assets/1786736f-f061-434e-ae74-fb33e16ff0d0" />


### 🔹 Prediction Result

<img width="1894" height="726" alt="result" src="https://github.com/user-attachments/assets/c071dd1c-4b3f-4012-be23-0876225c3292" />


---

## 🛠️ Tech Stack

* **Language**: Python
* **Libraries**: Pandas, NumPy, Scikit-learn
* **Backend**: Flask
* **Frontend**: HTML5, CSS3

---

## 📂 Project Structure

```bash
car-price-prediction-system/
│── app.py                      # Flask application
│── train.py                    # Model training
│── evaluate_model.py           # Model evaluation
│── create_data.py              # Synthetic data generation
│── process_real_data.py        # Real data preprocessing
│── car_price_model.pkl         # Trained ML model
│── car_price_predictor.ipynb   # Jupyter Notebook (analysis)
│── Car_Price_Prediction.csv    # Synthetic dataset
│── Car_Price_Prediction_Real.csv # Real dataset
│── requirements.txt
│── README.md
│
│── templates/
│    └── index.html            # Frontend UI
│
│── static/
│    ├── input.png             # Screenshot - input UI
│    ├── result.png            # Screenshot - output
│    ├── style.css             # Styling
│    ├── Hyundai.png           # Car images
│    ├── Kia.png
│    ├── Tata.png
│    └── ...                   # Other brand images
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/OmChuri/car-price-prediction-system.git
cd car-price-prediction-system
```

### 2. Create Virtual Environment

```bash
py -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train Model (Optional)

```bash
py train.py
```

### 5. Run Application

```bash
py app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Performance

| Metric   | Value       |
| -------- | ----------- |
| R² Score | ~97.5%      |
| MAE      | ~₹1.06 Lakh |
| RMSE     | ~₹1.48 Lakh |

👉 The model performs well and predicts prices with low error.

---

## ⚠️ Limitations

* Dataset is **synthetic / limited**
* Possible **overfitting due to high accuracy**
* Needs validation on real-world data

---

## 🚀 Future Improvements

* Use larger real-world datasets
* Add more features (location, ownership, etc.)
* Deploy on cloud (Render / AWS)
* Add REST API

---

## 🏷️ Topics

machine-learning, flask, random-forest, regression, data-science, car-price-prediction

---

## 👨‍💻 Author

**Om Churi**
📧 [omchuri2005@gmail.com](mailto:omchuri2005@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/om-churi
💻 GitHub: https://github.com/OmChuri


