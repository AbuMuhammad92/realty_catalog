from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="test_nf_group",
    user="abumuhhamad",
    host="localhost"
)

@app.route('/')
def index():
    area = request.args.get('area')
    floor = request.args.get('floor')
    metro = request.args.get('metro')

    query = "SELECT * FROM properties WHERE TRUE"
    params = []

    if area:
        try:
            area = float(area.replace(" м²", "").replace(",", "."))
            query += " AND area >= %s"
            params.append(area)
        except ValueError:
            pass

    if floor:
        query += " AND floor = %s"
        params.append(floor)
    if metro:
        query += " AND %s = ANY(metro)"
        params.append(metro)

    with conn.cursor() as cursor:
        cursor.execute(query, tuple(params))
        properties = cursor.fetchall()

    return render_template('index.html', properties=properties)



@app.route('/property/<int:property_id>')
def property_details(property_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM properties WHERE id = %s", (property_id,))
        property = cursor.fetchone()
    return render_template('details.html', property=property)


if __name__ == '__main__':
    app.run(debug=True)
