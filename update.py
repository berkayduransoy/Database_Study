import sqlite3

conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

update_query = """
UPDATE CARS
SET daily_price = daily_price * 0.95
WHERE daily_price > 8000; """

# Sorguyu çalıştır
cursor.execute(update_query)

# Değişiklikleri kaydet
conn.commit()

# Güncellenmiş verileri kontrol etmek için tüm araçları çek ve yazdır
cursor.execute("SELECT * FROM CARS WHERE daily_price > 8000;")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()