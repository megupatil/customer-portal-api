from database import get_connection

def get_orders_by_email(email, start_date, end_date):

    conn = get_connection()

    cursor = conn.cursor()

    query = (
        "SELECT * FROM orders WHERE email = '"
        + email
        + "' AND order_date BETWEEN '"
        + start_date
        + "' AND '"
        + end_date
        + "'"
    )

    cursor.execute(query)

    results = cursor.fetchall()

    conn.close()

    return results
