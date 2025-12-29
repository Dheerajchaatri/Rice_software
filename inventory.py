import streamlit as st
from database import get_db

def update_inventory(variety, qty, rate):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT quantity, avg_cost FROM inventory WHERE variety=?",
        (variety,)
    )
    row = cur.fetchone()

    if row:
        old_qty, old_cost = row
        new_qty = old_qty + qty
        new_cost = ((old_qty * old_cost) + (qty * rate)) / new_qty

        cur.execute("""
        UPDATE inventory
        SET quantity=?, avg_cost=?
        WHERE variety=?
        """, (new_qty, new_cost, variety))
    else:
        cur.execute("""
        INSERT INTO inventory (variety, quantity, avg_cost)
        VALUES (?, ?, ?)
        """, (variety, qty, rate))

    conn.commit()
    conn.close()

# ---------- Streamlit UI ----------
st.title("Update Rice Inventory")

variety = st.text_input("Rice Variety")
qty = st.number_input("Quantity", min_value=0.0, step=1.0)
rate = st.number_input("Rate per Unit", min_value=0.0, step=0.1)

if st.button("Update Inventory"):
    if variety and qty > 0:
        update_inventory(variety, qty, rate)
        st.success("Inventory updated successfully")
    else:
        st.error("Enter valid variety and quantity")
