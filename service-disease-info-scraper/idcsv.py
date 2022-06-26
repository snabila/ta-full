import sqlite3
import csv
import pandas as pd

# open connection to sqlite database
conn = sqlite3.connect('test2.db')
c = conn.cursor()

# drop old table
c.execute('''DROP TABLE disease_info_id''')

# make a new table, comment after one run
c.execute('''CREATE TABLE disease_info_id(
    pk INTEGER NOT NULL PRIMARY KEY,
    disease_name TEXT,
    overview TEXT,
    symptoms TEXT,
    when_to_see_doctor TEXT,
    causes TEXT,
    risk_factors TEXT,
    complication TEXT,
    prevention TEXT
)''')

data = pd.read_csv('testID.csv')

data.to_sql('disease_info_id', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Done")
