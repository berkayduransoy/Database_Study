import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE (
               employee_id INTEGER PRIMARY KEY,
               name TEXT,
               lastname TEXT,
               age INTEGER,
               phone TEXT,
               email TEXT,
               qualification TEXT,
               address TEXT,
               city TEXT,
               salary REAL,
               role TEXT
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS CUSTOMER (
               customer_id INTEGER PRIMARY KEY,
               name TEXT,
               lastname TEXT,
               gender TEXT,
               license TEXT,
               phone TEXT,
               address TEXT,
               city TEXT,
               street TEXT,
               branch_id INTEGER,
               FOREIGN KEY(branch_id) REFERENCES BRANCH(branch_id)
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS BRANCH (
               branch_id INTEGER PRIMARY KEY,
               name TEXT,
               address TEXT,
               city TEXT,
               street TEXT
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS CARS (
               car_id INTEGER PRIMARY KEY,
               model TEXT,
               plate TEXT,
               daily_price REAL,
               color TEXT,
               year INTEGER,
               employee_id INTEGER,
               deleted integer DEFAULT 0,
               FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id)
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS RENT (
               rent_id INTEGER PRIMARY KEY,
               pay_date TEXT,
               pay_method TEXT,
               damage_composition TEXT,
               customer_id INTEGER,
               car_id INTEGER,
               FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id),
               FOREIGN KEY(car_id) REFERENCES CARS(car_id)
               )""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS RESERVATION (
               reservation_id INTEGER PRIMARY KEY,
               reservate_date TEXT,
               pickup_date TEXT,
               days INTEGER,
               customer_id INTEGER,
               FOREIGN KEY(customer_id) REFERENCES CUSTOMER(customer_id)
               )""")

fake = Faker()

# EMPLOYEE tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute("""INSERT INTO EMPLOYEE (name, lastname, age, phone, email, qualification, address, city, salary, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, 
              (fake.first_name(),
               fake.last_name(), 
               random.randint(0,100), 
               fake.phone_number(), 
               fake.email(),
               fake.job(), 
               fake.address(), 
               fake.city(), 
               round(random.uniform(17002, 100000), 2), 
               fake.job())
             )

# CUSTOMER tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute(""" INSERT INTO CUSTOMER (name, lastname, gender, license, phone, address, city, street, branch_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) """,
              (fake.first_name(),
               fake.last_name(),
               random.choice(['Male', 'Female']),
               fake.license_plate(), 
               fake.phone_number(),
               fake.address(),
               fake.city(),
               fake.street_name(),
               random.randint(1, 10))
             )

# BRANCH tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute(""" INSERT INTO BRANCH (name, address, city, street) VALUES (?, ?, ?, ?) """,
              (fake.company(),
               fake.address(),
               fake.city(),
               fake.street_name())
             )

# CARS tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute(""" INSERT INTO CARS (model, plate, daily_price, color, year, employee_id) VALUES (?, ?, ?, ?, ?, ?) """,
              (fake.word(),
               fake.license_plate(), 
               round(random.uniform(3000, 10000), 2), 
               fake.color_name(), 
               random.randint(2000, 2024), 
               random.randint(1, 100))
             )

# RENT tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute(""" INSERT INTO RENT (pay_date, pay_method, damage_composition, customer_id, car_id) VALUES (?, ?, ?, ?, ?) """,
              (fake.date_this_decade(), 
               random.choice(['Credit Card', 'Cash', 'EFT']), 
               fake.sentence(),
               random.randint(1, 100), 
               random.randint(1, 100))
             )

# RESERVATION tablosuna 100 veri ekleme
for _ in range(100):
    cursor.execute(""" INSERT INTO RESERVATION (reservate_date, pickup_date, days, customer_id) VALUES (?, ?, ?, ?)""",
              (fake.date_this_year(), 
               fake.date_this_year(), 
               random.randint(1, 30), 
               random.randint(1, 100))
             )
fake = Faker()

conn.commit()
conn.close()
