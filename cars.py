from tkinter import *
import sqlite3

root = Tk()
root.title("Car Database")
root.geometry("1000x1000")


def create_tables():
    conn = sqlite3.connect("cars_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            name TEXT,
            year INTEGER,
            engine TEXT,
            price REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS features (
            id INTEGER PRIMARY KEY,
            car_id INTEGER,
            feature_name TEXT,
            feature_description TEXT,
            FOREIGN KEY (car_id) REFERENCES cars (id)
        )
    ''')

    conn.commit()
    conn.close()

create_tables()


def add_car(name, year, engine, price):
    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cars (name, year, engine, price) VALUES (?, ?, ?, ?)
    ''', (name, year, engine, price))
    conn.commit()
    conn.close()


def add_features(car_id, feature_name, feature_description):
    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO features (car_id, feature_name, feature_description) VALUES (?, ?, ?)
    ''', (car_id, feature_name, feature_description))
    conn.commit()
    conn.close()


def show_cars():
    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, year, engine, price FROM cars")
    cars = cursor.fetchall()

    car_list.delete(0, END)  
    for car in cars:
        car_list.insert(END, f"ID: {car[0]}, Name: {car[1]}, Year: {car[2]}, Engine: {car[3]}, Price: {car[4]}")
    
    conn.close()


def show_features(event):
    selected_car = car_list.get(car_list.curselection())
    car_id = int(selected_car.split(",")[0].split(":")[1].strip())

    conn = sqlite3.connect("cars_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT feature_name, feature_description FROM features WHERE car_id=?", (car_id,))
    features = cursor.fetchall()
    
    feature_list.delete(0, END)
    for feature in features:
        feature_list.insert(END, f"{feature[0]}: {feature[1]}")
    
    conn.close()

def add_initial_cars():
    cars = [
        ("Peugeot Pars", 2022, "XU7P - 100 hp, 153 Nm", []),
        ("Samand LX", 2022, "EF7 - 115 hp, 157 Nm", ["Air Conditioning", "ABS", "Electric Windows"]),
        ("Dena Plus", 2022, "EF7 Turbo - 150 hp, 215 Nm", ["Touch Screen", "Cruise Control", "Rear View Camera"]),
        
        ("BMW M5 E28", 1984, "3.5L I6 - 282 hp, 340 Nm", ["Leather Seats", "Air Conditioning"]),
        ("BMW M5 E34", 1988, "3.6L I6 - 311 hp, 360 Nm", ["Sunroof", "ABS", "Leather Interior"]),
        ("BMW M5 E39", 1998, "4.9L V8 - 394 hp, 500 Nm", ["Navigation", "Cruise Control", "Heated Seats"]),
        ("BMW M5 E60", 2005, "5.0L V10 - 500 hp, 520 Nm", ["Dynamic Stability Control", "Head-Up Display"]),
        ("BMW M5 F10", 2011, "4.4L V8 - 560 hp, 680 Nm", ["Adaptive LED Lights", "Parking Assistant"]),
        ("BMW M5 F90", 2018, "4.4L V8 - 600 hp, 750 Nm", ["Touch Screen Display", "Gesture Control", "Remote Start"])
    ]

    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()

    for car in cars:

        cursor.execute("SELECT * FROM cars WHERE name = ? AND year = ? AND engine = ?", (car[0], car[1], car[2]))
        result = cursor.fetchone()

        if result is None: 
            cursor.execute('''INSERT INTO cars (name, year, engine, price) VALUES (?, ?, ?, ?)''', (car[0], car[1], car[2], None))
            car_id = cursor.lastrowid

            for feature in car[3]:
                cursor.execute('''INSERT INTO features (car_id, feature_name, feature_description) VALUES (?, ?, ?)''', (car_id, feature, ""))
            
    conn.commit()
    conn.close()


add_initial_cars()


car_list = Listbox(root, width=85, height=25)
car_list.pack(pady=10)
car_list.bind('<<ListboxSelect>>', show_features)

btn_show_cars = Button(root, text="Show Cars", command=show_cars)
btn_show_cars.pack(pady=5)

feature_list = Listbox(root, width=85, height=25)
feature_list.pack(pady=10)

root.mainloop()
