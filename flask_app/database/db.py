import pymysql
import json
import os

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "NeoG352912"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('querys.json', 'r', encoding="UTF-8") as querys:
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

def get_id_comuna_by_nombre(nombre_comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_nombre"], (nombre_comuna,))
	comuna = cursor.fetchone()
	return comuna

get_id_comuna_by_nombre("Independecia")
create_user("Juan Carlos Bodoque", "juan.carlos@31minutos.cl", "012345678", 130216, "2024-09-31 23:59:07")