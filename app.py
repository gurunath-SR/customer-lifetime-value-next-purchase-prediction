import streamlit as st
import pandas as pd
import joblib
import os

# ==========================================
# LOAD MODELS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

clv_model = joblib.load(
    os.path.join(BASE_DIR, "models", "clv_model.pkl")
)

purchase_model = joblib.load(
    os.path.join(BASE_DIR, "models", "purchase_model.pkl")
)

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Customer Intelligence System",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Lifetime Value & Purchase Prediction")

st.markdown(
    """
    Predict:
    - 💰 Future Customer Lifetime Value
    - 🔄 Future Purchase Probability
    """
)

st.divider()

# ==========================================
# INPUTS
# ==========================================

st.subheader("Customer Information")

recency = st.number_input(
    "Recency (Days Since Last Purchase)",
    min_value=0,
    value=30
)

frequency = st.number_input(
    "Frequency (Number of Orders)",
    min_value=1,
    value=5
)

past_revenue = st.number_input(
    "Past Revenue",
    min_value=0.0,
    value=1000.0
)

avg_order_value = st.number_input(
    "Average Order Value",
    min_value=0.0,
    value=100.0
)

total_quantity = st.number_input(
    "Total Quantity Purchased",
    min_value=0,
    value=50
)

avg_quantity = st.number_input(
    "Average Quantity Per Order",
    min_value=0.0,
    value=10.0
)

active_days = st.number_input(
    "Active Days",
    min_value=0,
    value=100
)

segment = st.selectbox(
    "Customer Segment",
    [
        "Champions",
        "Lost Customers",
        "Loyal Customers",
        "Potential Loyalists"
    ]
)

# ==========================================
# PREDICT BUTTON
# ==========================================

if st.button("Predict"):

    # --------------------------------------
    # CLV FEATURES
    # --------------------------------------

    clv_input = pd.DataFrame({

        "Recency": [recency],
        "Frequency": [frequency],
        "PastRevenue": [past_revenue],
        "AvgOrderValue": [avg_order_value],
        "TotalQuantity": [total_quantity],
        "AvgQuantity": [avg_quantity],
        "ActiveDays": [active_days],

        "Segment_Champions":
            [1 if segment == "Champions" else 0],

        "Segment_Lost Customers":
            [1 if segment == "Lost Customers" else 0],

        "Segment_Loyal Customers":
            [1 if segment == "Loyal Customers" else 0],

        "Segment_Potential Loyalists":
            [1 if segment == "Potential Loyalists" else 0]

    })

    # --------------------------------------
    # PURCHASE FEATURES
    # --------------------------------------

    purchase_input = pd.DataFrame({

        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [past_revenue],
        "TotalQuantity": [total_quantity]

    })

    # --------------------------------------
    # PREDICTIONS
    # --------------------------------------

    clv_prediction = clv_model.predict(
        clv_input
    )[0]

    purchase_prediction = purchase_model.predict(
        purchase_input
    )[0]

    purchase_probability = purchase_model.predict_proba(
        purchase_input
    )[0][1]

    st.divider()

    st.subheader("📈 Prediction Results")

    st.metric(
        "Predicted Future CLV",
        f"{clv_prediction:.2f}"
    )

    st.metric(
        "Purchase Probability",
        f"{purchase_probability*100:.2f}%"
    )

    if purchase_prediction == 1:
        st.success(
            "✅ Customer is likely to purchase again."
        )
    else:
        st.error(
            "⚠️ Customer is unlikely to purchase again."
        )