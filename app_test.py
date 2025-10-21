import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM TEST;")
print(cur.fetchone())

cur.close()
conn.close()
