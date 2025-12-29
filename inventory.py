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

