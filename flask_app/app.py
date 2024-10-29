from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_user, validate_device, validate_file
from database import db
from datetime import datetime
from werkzeug.utils import secure_filename
import hashlib
import os
import filetype
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ----- pagina principal -----
@app.route("/")
def index():
    return render_template("html/index.html") ## AGREGAR REDIRECT

@app.route("/agregar-donacion") ## NOMBRE DEL URL
def agregarDonacion():
    return render_template("html/agregar-donacion.html")

@app.route("/confirmar", methods=["POST"])
def confirmarForm():
    # VALIDAR USER
    name   = request.form.get("username")
    email  = request.form.get("email")
    phone  = request.form.get("phone-number")
    region = request.form.get("select-region")
    comuna = request.form.get("select-comuna")

    if validate_user(name, email, phone, region, comuna):
        fecha_creacion = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        contacto_id = db.create_user(name.lower(), email.lower(), phone, int(comuna), fecha_creacion)
    else: # para debugear
        error="Hay un error! (user)"
        print(error)
        return render_template("html/agregar-donacion.html",error=error)
    
    # VALIDAR CADA DISPOSITIVO
    device  = request.form.getlist("device-name") #lista con los nombres de cada dispositivo
    descrip = request.form.getlist("device-descr")
    tipo    = request.form.getlist("device-type")
    anhos   = request.form.getlist("years-of-use")
    estado  = request.form.getlist("working-status")
    
    for i in range(len(device)):
        input_name = 'device-pics-' + str(i+1)
        fotos   = request.files.getlist(input_name) #retorna una lista de FileStorage

        if validate_device(device[i], descrip[i], tipo[i], anhos[i], estado[i], fotos):          
            device_id = db.create_device(contacto_id, device[i], descrip[i], tipo[i], anhos[i], estado[i]) ##SE DUPLICA
            
            ## craer path para imagenes
            for foto in fotos:
                # 1. generate random name for img
                _filename = hashlib.sha256(
                    secure_filename(foto.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(foto).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

                # 2. save img as a file
                foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

                ruta = os.path.join(UPLOAD_FOLDER, img_filename) 

                db.create_file(ruta, img_filename, device_id)
                
        else: #para debugear
            error="Se produjo un error al subir los archivos, vuelva a intentarlo."
            print(error)
            return render_template("html/agregar-donacion.html",error=error)
    
    success_message = "Hemos recibido la información de su donación. Muchas gracias."
    return render_template("html/agregar-donacion.html", success_message=success_message)


@app.route("/ver-dispositivos/<page>", methods=["GET"])
def verDispositivos(page):
    #obtener los datos de la db, elegir según que botón se presione
    FIRST = (int(page)-1)*5
    data = []
    for device in db.get_dispositivos(FIRST):
        device_id, contacto_id, nombre_disp, _, tipo, _, estado = device
        _, _, _, _, comuna_id, _ = db.get_user_by_id(contacto_id)

        comuna, _ = db.get_region_comuna_by_id_comuna(comuna_id)

        nombre_arc, = db.get_file_by_device_id(device_id)
        print("ver dipositivos:", device_id, "-", nombre_arc)
        ruta_arch = f"uploads/{nombre_arc}"
        
        data.append({
            "device_id": device_id,
            "comuna": comuna, 
            "dispositivo": nombre_disp, 
            "tipo": tipo, 
            "estado": estado,
            "pic_path": url_for('static', filename=ruta_arch)
        })

    return render_template("html/ver-dispositivos.html", data=data, page=page)

@app.route("/informacion-dispositivo/<device_id>", methods=["GET"])
def verInfoDispositivo(device_id):
    #obtenemos la info de la base de datos y mostramos

    _, contacto_id, nombre_disp, descr, tipo, anhos_uso, estado = db.get_device_by_id(device_id)
    _, nombre, email, celular, comuna_id, _ = db.get_user_by_id(contacto_id)

    nombre_arc, = db.get_file_by_device_id(device_id)
    ruta_arch = f"uploads/{nombre_arc}"
    comuna, region = db.get_region_comuna_by_id_comuna(comuna_id)

    data = {
        "nombre": nombre,
        "email": email,
        "telefono": celular, 
        "region": region, 
        "comuna": comuna,
        "dispositivo": nombre_disp,
        "descr": descr,
        "tipo": tipo,
        "anhos": anhos_uso,
        "estado": estado,
        "pic_path": url_for('static', filename=ruta_arch)
    }
    return render_template("html/informacion-dispositivo.html", data=data, device_id=device_id)

if __name__ == "__main__":
    app.run(debug=True)