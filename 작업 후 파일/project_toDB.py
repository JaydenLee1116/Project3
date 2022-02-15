import sqlite3

conn = sqlite3.connect('project.db')

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS aptvil2021;")

cur.execute("""CREATE TABLE aptvil2021(
    Id INTEGER,
    dealAmountYear INTEGER,
    buildYear INTEGER,
    dong VARCHAR(128),
    areaForExclusiveUse FLOAT,
    floor INTEGER,
    kinds VARCHAR(128),
    region VARCHAR(128),
    PRIMARY KEY(Id)
    )"""
    )

import csv


with open('data_final.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO aptvil2021 VALUES (?, ?, ?, ?, ?, ?, ?, ?)" , (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        

conn.commit()

cur.close()
conn.close()