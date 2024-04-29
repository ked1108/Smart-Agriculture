import psycopg2

CONNECTION = "postgres://postgres:kedu1108@localhost:5432/tsdb"
conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

query_create_sensordata_table = """
CREATE TABLE IF NOT EXISTS sensorsdata(
    id SERIAL PRIMARY KEY,
    time TIMESTAMPTZ NOT NULL,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    soil_moisture INTEGER,
    height DOUBLE PRECISION
)
"""

def insert(temp, hum, soil, height):
    if temp != None and hum != None and soil!= None and height!= None:
        cursor.execute("INSERT INTO sensorsdata(time, temperature, humidity, soil_moisture, height) VALUES (now(), {0}, {1}, {2}, {3})".format(temp, hum, soil, height))
    else:
        cursor.execute("INSERT INTO sensorsdata(time, temperature, humidity, soil_moisture, height) VALUES (now(), NULL, NULL, {2}, {3})".format(temp, hum, soil, height))
    conn.commit()
    print("DB Inserted")

if __name__ == "__main__":
    cursor.execute(query_create_sensordata_table)
    conn.commit()

