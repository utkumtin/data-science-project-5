import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password=password
    )

# 1- Null emailleri 'unknown@example.com' ile değiştir
def clean_null_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE customers
                SET email = COALESCE(email, 'unknown@example.com');
            """)
            conn.commit()

# 2- Hatalı emailleri bul
def find_invalid_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM customers
                WHERE email NOT LIKE '%@%';
            """)
            return cur.fetchall()

# 3- İsimlerin ilk 3 harfi
def get_first_3_letters_of_names():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT full_name, LEFT(full_name, 3) AS short_name
                FROM customers;
            """)
            return cur.fetchall()

# 4- Email domainlerini bul
def get_email_domains():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT full_name, RIGHT(email, LENGTH(email) - POSITION('@' IN email)) AS domain
                FROM customers;
            """)
            return cur.fetchall()

# 5- İsim ve email birleştir
def concat_name_and_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT CONCAT(full_name, ' - ', email) AS full_info
                FROM customers;
            """)
            return cur.fetchall()

# 6- Sipariş tutarlarını tam sayıya çevir
def cast_total_amount_to_integer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT order_id, CAST(total_amount AS INTEGER) AS total_amount_int
                FROM orders;
            """)
            return cur.fetchall()

# 7- Email '@' pozisyonu
def find_at_position_in_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT full_name, STRPOS(email, '@') AS at_position
                FROM customers;
            """)
            return cur.fetchall()

# 8- NULL kategoriye 'Unknown' yaz
def fill_null_product_category():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT product_name, COALESCE(category, 'Unknown') AS product_category
                FROM products;
            """)
            return cur.fetchall()

# 9- Müşteri harcama sıralaması (RANK)
def rank_customers_by_spending():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT customer_id, total_amount,
                       RANK() OVER (ORDER BY total_amount DESC) AS rank_by_spend
                FROM orders;
            """)
            return cur.fetchall()

# 10- Müşteri siparişlerinde running total
def running_total_per_customer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT order_id, customer_id, total_amount,
                       SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS running_total
                FROM orders;
            """)
            return cur.fetchall()

# 11- Elektronik ve Beyaz Eşya ürünleri (UNION)
def get_electronics_and_appliances():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT product_name, 'Electronics' AS type
                FROM products
                WHERE category = 'Electronics'
                UNION
                SELECT product_name, 'Appliances' AS type
                FROM products
                WHERE category = 'Appliances';
            """)
            return cur.fetchall()

# 12- Tüm siparişler ve eksik siparişler (UNION ALL)
def get_orders_with_missing_customers():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT customer_id, total_amount
                FROM orders
                UNION ALL
                SELECT customer_id, 0
                FROM customers
                WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);
            """)
            return cur.fetchall()