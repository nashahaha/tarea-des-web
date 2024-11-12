import pymysql
import json
import os
from datetime import datetime

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

def create_user(nombre:str, email:str, celular:str, comuna_id: int, fecha_creacion):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["create_user"], (nombre, email, celular, comuna_id, fecha_creacion))
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID();")
    return cursor.fetchone()[0]
	

def create_device(contacto_id, nombre_disp, descr, tipo, anhos_uso, estado):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_device"], (contacto_id, nombre_disp, descr, tipo, anhos_uso, estado))
	conn.commit()
	cursor.execute("SELECT LAST_INSERT_ID();")
	return cursor.fetchone()[0]

def create_file(ruta, nombre_arc, dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_file"], (ruta, nombre_arc, dispositivo_id))
	conn.commit()

def create_comment(nombre_com: str, comm: str, fecha: str, device_id: int):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_comment"], (nombre_com, comm, fecha, device_id))
	conn.commit()

def get_id_comuna_by_nombre(nombre_comuna): #no se usa
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_nombre"], (nombre_comuna,))
	comuna = cursor.fetchone()
	return comuna

def get_dispositivos(start: int):
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

def get_device_by_contacto_id(contacto_id: int): ## malo, un contacto puede tener multiples dispositivos
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_device_by_contacto_id"], (contacto_id))
	device = cursor.fetchone()
	return device

def get_device_by_id(device_id: int):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_device_by_id"], (device_id))
	device = cursor.fetchone()
	return device

def get_file_by_device_id(device_id: int):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_files_from_device"], (device_id,))
	file = cursor.fetchone()
	return file

def get_comments_by_device_id(device_id: int):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comments_by_device_id"], (device_id,))
	comm_list = cursor.fetchall()
	return comm_list

def get_comunas_id():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM comuna;")
	comunas_list = cursor.fetchall()
	return comunas_list

def count_devices_by_comuna(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["count_devices_by_comuna"], (comuna_id,))
	devices_num = cursor.fetchone()
	return devices_num

def get_nombre_comuna(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_nombre_comuna"], (comuna_id,))
	nom_comuna, = cursor.fetchone()
	return nom_comuna

def count_devices_by_type(tipo):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["count_devices_by_type"], (tipo,))
	devices_num, = cursor.fetchone()
	return devices_num

def count_dev_data():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) AS total_rows FROM dispositivo;")
	devices, = cursor.fetchone()
	return devices
	