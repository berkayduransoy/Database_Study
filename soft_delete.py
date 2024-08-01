

soft_delete_query = """
UPDATE CARS
SET is_deleted = 1
WHERE car_id = 1 AND color = 'White'; """

cursor.execute(soft_delete_query)
conn.commit()

cursor.execute("SELECT * FROM CARS WHERE is_deleted = 1;")
deleted_cars = cursor.fetchall()

# Sonuçları yazdır
for car in deleted_cars:
    print(car)
