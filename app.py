from flask import Flask, jsonify, render_template_string, request
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    'host': '127.0.0.1',
    'database': 'postgres',       
    'user': 'postgres',         
    'password': '12345678',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def home():
    rows = get_users()

    html = """
    <html>
        <head><title>Flask + PostgreSQL</title></head>
        <body style="font-family: sans-serif;">
            <h2>รายชื่อผู้ใช้จากตาราง test</h2>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>ID</th><th>Name</th><th>Age</th></tr>
                {% for id, name, age in rows %}
                    <tr>
                        <td>{{ id }}</td>
                        <td>{{ name }}</td>
                        <td>{{ age }}</td>
                    </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """

    return render_template_string(html, rows=rows)

@app.route('/users')
# def get_users():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT id, name, age FROM test;')  
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

def get_users():
    name = request.args.get('name')  
    conn = get_db_connection()
    cur = conn.cursor()

    if name:  
        cur.execute('SELECT id, name, age FROM test WHERE name = %s ORDER BY id;', (name,))
    else:   
        cur.execute('SELECT id, name, age FROM test ORDER BY id;')

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

if __name__ == '__main__':
    app.run(debug=True)
