import sqlite3

conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

query = """ SELECT 
    CUSTOMER.customer_id,
    CUSTOMER.name,
    CUSTOMER.lastname,
    AVG(CARS.daily_price) AS average_daily_price
    FROM CUSTOMER
    JOIN RENT ON CUSTOMER.customer_id = RENT.customer_id
    JOIN CARS ON RENT.car_id = CARS.car_id
    GROUP BY CUSTOMER.customer_id, CUSTOMER.name, CUSTOMER.lastname; """

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Customer ID: {row[0]}, Name: {row[1]} {row[2]}, Average Daily Price: {row[3]:.2f}")

conn.close()