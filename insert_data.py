# Parses the contents in 'global_sealevel.csv' and insert into database

import psycopg2
import csv

# Database connection - PostgresSQL
password = open('***')
dsn = f'user=*** password={***} dbname=***'
conn = psycopg2.connect(dsn)
cur = conn.cursor()

sql = """INSERT INTO sea_level (year, sea_level) VALUES"""

# Loop through CSV data
with open('global_sealevel.csv') as data:
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        year = round(float(row[0]))
        level = float(row[1])
        sql += f' ({year}, {level}),'

# Remove trailing whitespace and comma
sql = sql.strip(',') + ';'

# Execute sql
cur.execute(sql)
conn.commit()

# Close file, cursor, and connection
password.close()
cur.close()
conn.close()
