import psycopg2
import random
from faker import Faker

# Initialize Faker to generate random names
fake = Faker()

# Database connection
def connect_db():
    conn = psycopg2.connect(
        dbname='warehouse',  
        user='postgres',       
        password='asdASD123123',  
        host='172.29.48.1',       
        port='5433'
    )
    return conn

# Simulate Inventory Data
def generate_inventory_data():
    conn = connect_db()
    cur = conn.cursor()
    for _ in range(100):  # Generate 100 entries
        product_name = fake.word()
        quantity_in_stock = random.randint(50, 200)
        quantity_defective = random.randint(0, 10)
        cur.execute(
            "INSERT INTO inventory_data (product_name, quantity_in_stock, quantity_defective) VALUES (%s, %s, %s)",
            (product_name, quantity_in_stock, quantity_defective)
        )
    conn.commit()
    cur.close()
    conn.close()

# Simulate Defect Trend Data
def generate_defect_data():
    conn = connect_db()
    cur = conn.cursor()
    for _ in range(50):  # Generate 50 defect types
        defect_type = fake.word()
        occurrence_count = random.randint(1, 100)
        cur.execute(
            "INSERT INTO defect_trends (defect_type, occurrence_count) VALUES (%s, %s)",
            (defect_type, occurrence_count)
        )
    conn.commit()
    cur.close()
    conn.close()

# Generate data
generate_inventory_data()
generate_defect_data()
