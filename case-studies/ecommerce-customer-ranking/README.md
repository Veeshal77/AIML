# eCommerce Customer Ranking Using BigQuery ML  
### End-to-End Machine Learning Case Study

This project builds a **logistic regression propensity-ranking model** using BigQuery ML to identify customers most likely to purchase on a return visit. Instead of binary classification, the solution reframes the problem as **Top‑K ranking**, enabling high-ROI marketing activation.

---

## 🛒 Problem Statement
Millions of raw Google Analytics records contain valuable behavioral signals.  
Binary classification fails due to extreme class imbalance (only ~0.6% convert).  
This project reframes the task:

> Rank customers by purchase likelihood and target the top-K highest propensity users.

---

## 📊 Dataset
- **Source:** Google Merchandise Store Analytics (BigQuery Public Datasets)  
- **Time Range:** 2016–2017  
- **Records:** 3.3M+  
- **Train:** 2.5M+  
- **Test:** 470K  
- **Target:** `will_buy_on_return_visit`

---

## 🛠 Feature Engineering
Features include:

- **latest_ecommerce_progress**  
- **bounces**  
- **time_on_site**  
- **pageviews**  
- **traffic source / medium / channel grouping**  
- **device category**  
- **country**

---

## 🧱 Architecture & Workflow
1. Data ingestion  
2. SQL-based cleaning (new visits only)  
3. Feature creation using `MAX(action_type)`  
4. Logistic regression training  
5. Evaluation using ROC_AUC  
6. Propensity scoring using `ML.PREDICT`

---

## 📈 Model Performance
| Metric | Value | Notes |
|--------|--------|-------|
| **ROC_AUC** | 0.92 | Strong separation of buyers vs non-buyers |
| **Accuracy** | 0.97 | Not useful due to imbalance |
| **Precision/Recall/F1** | Low | Expected; ignored for ranking |

---

## 💡 Business Insights
- Top 6% of visitors → **6%+ conversion rate**  
- Overall conversion → **0.6%**  
- Targeting top 6% → **9× ROI improvement**  
- Zero infrastructure overhead  
- Scalable to 2018–2026 with one query change  

---

## 📁 Files
- `Ecommerce_Customer_Ranking_BQML.pdf` — Full case study  
- `assets/screenshots/` — BigQuery UI screenshots

---
