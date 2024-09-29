import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

def create_user(nombre, email, celular, comuna_id, fecha_creacion):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["create_user"], (nombre, email, celular, comuna_id, fecha_creacion))
    conn.commit()

