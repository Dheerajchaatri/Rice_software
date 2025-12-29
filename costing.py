import streamlit as st

st.title("Max Purchase Rate Calculator")

# Inputs
sale_rate = st.number_input("Sale Rate", min_value=0.0, step=0.1)
profit = st.number_input("Profit", min_value=0.0, step=0.1)
processing = st.number_input("Processing Cost", min_value=0.0, step=0.1)

st.subheader("Purchase Distribution")

full_p = st.number_input("Full Purchase %", min_value=0.0, step=0.1)
short_p = st.number_input("Short Purchase %", min_value=0.0, step=0.1)
b2_p = st.number_input("B2 Purchase %", min_value=0.0, step=0.1)
b3_p = st.number_input("B3 Purchase %", min_value=0.0, step=0.1)

def max_purchase_rate(
    sale_rate,
    profit,
    processing,
    full_p, short_p, b2_p, b3_p
):
    factors = {
        "full": 1.0,
        "short": 0.5,
        "b2": 0.4,
        "b3": 0.3
    }

    effective_sale = (
        full_p * factors["full"] +
        short_p * factors["short"] +
        b2_p * factors["b2"] +
        b3_p * factors["b3"]
    ) * sale_rate

    max_rate = effective_sale - profit - processing
    return round(max_rate, 2)

if st.button("Calculate"):
    result = max_purchase_rate(
        sale_rate, profit, processing,
        full_p, short_p, b2_p, b3_p
    )
    st.success(f"Max Purchase Rate: {result}")
