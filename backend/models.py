def get_inventory_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT product_name, quantity_in_stock, quantity_defective FROM inventory_data LIMIT 50")
    rows = cur.fetchall()
    return [{"product_name": row[0], "quantity_in_stock": row[1], "quantity_defective": row[2]} for row in rows]

def get_defect_trends(conn):
    cur = conn.cursor()
    cur.execute("SELECT defect_type, occurrence_count FROM defect_trends LIMIT 50")
    rows = cur.fetchall()
    return [{"defect_type": row[0], "occurrence_count": row[1]} for row in rows]
