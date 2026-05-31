# Customer Lifetime Value & Next Purchase Prediction

## Project Overview

This project predicts:

1. Customer Lifetime Value (CLV)
2. Whether a customer is likely to make another purchase

The project uses transaction-level e-commerce data and applies machine learning techniques for customer analytics and business decision-making.

## Objectives

* Analyze customer purchasing behavior
* Perform RFM (Recency, Frequency, Monetary) analysis
* Predict Customer Lifetime Value
* Predict Next Purchase Probability
* Generate actionable business insights

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Jupyter Notebook
* Git & GitHub

## Project Structure

data/
notebooks/
src/
models/
outputs/
dashboard/

---------------------------------------------------------------------------------------------
# 🧠 Customer Lifetime Value + Next Purchase Prediction

## 📌 Project Overview

This project builds an end-to-end **Customer Intelligence System** that helps businesses understand customer behavior, predict future revenue, and estimate purchase probability.

We combine:
- Customer Lifetime Value (CLV) Prediction
- Next Purchase Prediction
- RFM-Based Customer Segmentation

---

## 🎯 Objective

The goal of this project is to:

- Predict how much a customer will spend in the future (CLV)
- Predict whether a customer will make another purchase
- Segment customers based on purchasing behavior
- Enable data-driven marketing decisions

---

## 📊 Dataset

- Online Retail Transaction Dataset (~5,00,000+ records)
- Features:
  - InvoiceNo
  - StockCode
  - Quantity
  - InvoiceDate
  - UnitPrice
  - CustomerID
  - Country

---

## 🧹 Data Preprocessing

- Removed missing Customer IDs
- Removed cancelled orders
- Removed duplicates
- Handled negative quantities
- Created clean transactional dataset

---

## 👥 RFM Customer Segmentation

We used:

- **Recency** → Days since last purchase
- **Frequency** → Number of transactions
- **Monetary** → Total spending

### Customer Segments:
- Champions
- Loyal Customers
- Potential Loyalists
- At Risk Customers
- Lost Customers

---

## 🤖 Machine Learning Models

### 🔵 1. Customer Lifetime Value (Regression)

Goal: Predict future customer revenue

| Model | R² Score |
|------|--------:|
| Random Forest | **0.786** |
| XGBoost | 0.783 |
| Linear Regression | 0.249 |

---

### 🟢 2. Next Purchase Prediction (Classification)

Goal: Predict whether customer will buy again

| Model | Accuracy |
|------|--------:|
| Random Forest | **0.65** |
| XGBoost | 0.64 |

---

## 🧠 Key Features Engineered

- Recency
- Frequency
- Past Revenue
- Average Order Value
- Total Quantity Purchased
- Active Customer Lifespan
- Customer Segment (RFM-based)

---

## 📈 Key Insights

- Customer segmentation significantly improves prediction performance
- High-value customers (Champions) contribute disproportionately to revenue
- Future purchase behavior is moderately predictable (~65% accuracy)
- Future revenue prediction is a harder but realistic business problem (R² ~ 0.78)

---

## 💼 Business Impact

This system helps businesses:

- Identify high-value customers
- Predict future revenue contribution
- Improve targeted marketing campaigns
- Reduce customer churn
- Optimize retention strategies
- Increase overall profitability

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn

---

## 📌 Final Outcome

Built a complete **Customer Analytics Pipeline**:

1. Data Cleaning
2. RFM Segmentation
3. Customer Clustering
4. CLV Prediction (Regression)
5. Purchase Prediction (Classification)

---

## 🚀 Future Improvements

- Deep learning models for CLV
- Time-series based purchase forecasting
- Customer churn prediction model
- Deployment using Streamlit / Flask
- Dashboard using Power BI

---

## 📊 Author

Data Science Project by Gurunath 🚀

