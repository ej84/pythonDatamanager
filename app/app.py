from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response

app = Flask(__name__)


def cities_import() -> List[Dict]:
    """config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'citiesData'
    }"""  # I blocked this code line and used another one as below because I kept getting error.

    conn = mysql.connector.connect(host="db", user="root", password="root", database="citiesData")

    # connection = mysql.connector.connect(config) # Blocked for the same reason of config code above.
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


@app.route('/')
def index() -> str:
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
