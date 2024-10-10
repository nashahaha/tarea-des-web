import pymysql
import json
import os

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r', encoding="UTF-8") as querys:
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

def get_id_comuna_by_nombre(nombre_comuna): #no se usa
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_nombre"], (nombre_comuna,))
	comuna = cursor.fetchone()
	return comuna

def get_dispositivos(start):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_devices"], (start,))
	dispositivos = cursor.fetchall()
	return dispositivos #debería devolver una lista de listas con toda la info

def get_user_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_id"], (id,))
	user_info = cursor.fetchone()
	return user_info

def get_region_comuna_by_id_comuna(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region_comuna_by_id_comuna"], (comuna_id,))
	region_comuna = cursor.fetchone()
	return region_comuna
