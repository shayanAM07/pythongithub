from tkinter import *
import sqlite3
conn=sqlite3.connect("cars_databace.db")
cursor=conn.cursor()
cursor.execute(''' create table if not exists cars (
id INTEGER PRIMARY KEY ,
name TEXT,
year INTEGER,
engine TEXT,
price REAL,
)


 ''')

cursor.execute('''
create table fi not exists features (
id integer primary key,
car_id integer,
feature_name TEXT,
feature_descraiption TEXT,
forenign key (car_id) references cars (id)

)




 ''')
conn.commit()
conn.close()


def add_car(name, year, engine):
    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    insert into cars (name, year, engine) values (?,?,?)
 ''', (name, year , engine))
    conn.commit()
    conn.close()



def add_features(car_id, feature_name, feature_description):
    conn = sqlite3.connect('cars_database.db')
    cursor = conn.cursor()
    cursor.execute(''' insert in to features (car_id, feature_name,feature_descraiption) values (?,?,?)
    ''',(car_id,feature_name,feature_description))
    conn.commit()
    conn.close()


    