from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_user, validate_device
from database import db
from datetime import datetime

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

@app.route("/ver-dispositivos")
def verDispositivos():
    #obtener los datos de la db, elegir según que botón se presione
    FIRST = 0
    data = []
    for device in db.get_dispositivos(FIRST):
        _, contacto_id, nombre_disp, _, tipo, _, estado = device
        _, _, _, _, comuna_id, _ = db.get_user_by_id(contacto_id)

        comuna, region = db.get_region_comuna_by_id_comuna(comuna_id)

        # OBTENER IMAGENES !!!!!!
        
        data.append({
            "contacto_id": contacto_id,
            "comuna": comuna, 
            "dispositivo": nombre_disp, 
            "tipo": tipo, 
            "estado": estado 
        })

    return render_template("html/ver-dispositivos.html", data=data)

@app.route("/informacion-dispositivo/<contacto_id>", methods=["GET"])
def verInfoDispositivo(contacto_id):
    #obtenemos la info de la base de datos y mostramos

    nombre_disp, descr, tipo, anhos_uso, estado = db.get_device_by_contacto_id(contacto_id)
    _, nombre, email, celular, comuna_id, _ = db.get_user_by_id(contacto_id)

    comuna, region = db.get_region_comuna_by_id_comuna(comuna_id)

    # OBTENER IMAGENES !!!!!!

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
        "estado": estado 
    }
    return render_template("html/informacion-dispositivo.html", data=data, contacto_id=contacto_id)

@app.route("/confirmar", methods=["POST"])
def confirmarForm():
    name   = request.form.get("username")
    email  = request.form.get("email")
    phone  = request.form.get("phone-number")
    region = request.form.get("select-region")
    comuna = request.form.get("select-comuna")

    device  = request.form.getlist("device-name")
    descrip = request.form.getlist("device-descr")
    tipo    = request.form.getlist("device-type")
    anhos   = request.form.getlist("years-of-use") ##primero validar (como str), hacer strip() y luego pasar a int
    estado  = request.form.getlist("working-status")
    fotos   = request.files.getlist("device-pics") #duda

    if validate_user(name, email, phone, region, comuna):
        fecha_creacion = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        contacto_id = db.create_user(name.lower, email, phone, int(comuna), fecha_creacion)
    else: # para debugear
        error="Hay un error! (user)"
        print(error)
        return render_template("html/agregar-donacion.html",error=error)
    
    for i in range(len(device)):
        if validate_device(device[i], descrip[i], tipo[i], anhos[i], estado[i], fotos[i]):
            db.create_device(contacto_id, device[i], descrip[i], tipo[i], anhos[i], estado[i])
        else: #para debugear
            error="Hay un error! (device)"
            print(error)
            return render_template("html/agregar-donacion.html",error=error)
    return render_template("html/agregar-donacion.html")



if __name__ == "__main__":
    app.run(debug=True)