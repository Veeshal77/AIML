# Taxi Fare Prediction Using BigQuery ML  
### End-to-End Machine Learning Case Study

This project demonstrates a production-grade machine learning pipeline built entirely inside **Google BigQuery ML**, eliminating the need for external Python-based ML infrastructure. Using over **110M+ NYC TLC taxi trip records**, the model predicts taxi fares using SQL-only ML.

---

## 🚕 Problem Statement
Accurately estimating taxi fares is essential for both passengers and operators. Traditional ML workflows require exporting data to external environments, increasing cost and complexity.  
This project answers:

- Can we train a predictive fare model **directly on raw trip data** without data movement?
- Which trip attributes (distance, passengers, hour, borough) best predict fare?
- Can SQL-native ML match notebook-based pipelines?

---

## 📊 Dataset
- **Source:** NYC TLC Yellow Taxi Trips (BigQuery Public Datasets)
- **Time Range:** 2015–2016  
- **Total Records:** 800M+  
- **Train/Test:** 850K each  
- **Target:** `total_fare`

---

## 🛠 Feature Engineering
Key engineered features include:

- **trip_distance** — strongest predictor  
- **longitude/latitude deltas** — Euclidean distance  
- **passenger_count**  
- **pickup_hour**  
- **pickup_day_of_week**

Data cleaning filters remove outliers and invalid coordinates.

---

## 🧱 Architecture & Workflow
1. Data ingestion from BigQuery public datasets  
2. SQL-based cleaning  
3. Feature creation using `EXTRACT()`  
4. Model training using `CREATE MODEL` (Linear Regression)  
5. Evaluation using `ML.EVALUATE`  
6. Batch prediction using `ML.PREDICT`

---

## 📈 Model Performance
| Metric | Value | Meaning |
|--------|--------|---------|
| **RMSE** | 4.38 | Avg. prediction error in USD |
| **MAE** | 2.53 | Avg. absolute deviation |
| **R²** | 0.81 | 81% variance explained |

---

## 💡 Business Impact
- Fare transparency for passengers  
- Surge pricing calibration for operators  
- Zero infrastructure overhead  
- Scalable to 2017–2026 with one query change  

---

## 📁 Files
- `Taxi_Fare_Prediction_BQML.pdf` — Full case study  
- `assets/screenshots/` — BigQuery UI screenshots

---

