import streamlit as st
from costing import max_purchase_rate
from database import setup_db

# Initialize DB
setup_db()

st.set_page_config(page_title="رائس کاسٹنگ سافٹ ویئر")

st.title("رائس کاسٹنگ سافٹ ویئر")

# Inputs
sale = st.number_input("سیل ریٹ (Rs/kg)", min_value=0.0, step=0.1)
profit = st.number_input("منافع", min_value=0.0, step=0.1)
proc = st.number_input("پروسیسنگ خرچ", min_value=0.0, step=0.1)

st.subheader("شرح تقسیم (%)")

full = st.number_input("Full %", value=0.60, step=0.01)
short = st.number_input("Short %", value=0.15, step=0.01)
b2 = st.number_input("B2 %", value=0.20, step=0.01)
b3 = st.number_input("B3 %", value=0.05, step=0.01)

# Button
if st.button("MAX خریداری ریٹ نکالیں"):
    try:
        rate = max_purchase_rate(
            sale,
            profit,
            proc,
            full,
            short,
            b2,
            b3
        )
        st.success(f"زیادہ سے زیادہ خریداری ریٹ: {rate} Rs/kg")
    except:
        st.error("درست نمبر درج کریں")
