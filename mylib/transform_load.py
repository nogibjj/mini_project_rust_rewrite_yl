"""
Transforms and Loads data into the local SQLite3 database

"""

import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/candy-data.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("candy_data_DB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS candy_data_DB")
    c.execute(
        """
        CREATE TABLE candy_data_DB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            competitorname TEXT,
            chocolate INTEGER,
            fruity INTEGER,
            caramel INTEGER,
            peanutyalmondy INTEGER,
            nougat INTEGER,
            crispedricewafer INTEGER,
            hard INTEGER,
            bar INTEGER,
            pluribus INTEGER,
            sugarpercent FLOAT,
            pricepercent FLOAT,
            winpercent FLOAT
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO candy_data_DB(
            competitorname,
            chocolate,
            fruity,
            caramel,
            peanutyalmondy,
            nougat,
            crispedricewafer,
            hard,
            bar,
            pluribus,
            sugarpercent,
            pricepercent,
            winpercent) 
            VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "ServeTimesDB.db"


if __name__ == "__main__":
    load()
