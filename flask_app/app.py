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
    return render_template("html/index.html")

@app.route("/agregar-donacion") ## NOMBRE DEL URL
def agregarDonacion():
    return render_template("html/agregar-donacion.html")

@app.route("/ver-dispositivos")
def verDispositivos():
    #obtener los datos de la db, elegir según que botón se presione
    FIRST = 0
    data = []
    for device in db.get_dispositivos(FIRST):
        _, contacto_id, nombre_disp, descripcion, tipo, anhos_uso, estado = device
        _, nombre, email, celular, comuna_id, _ = db.get_user_by_id(contacto_id)

        comuna, region = db.get_region_comuna_by_id_comuna(comuna_id)

        # OBTENER IMAGENES !!!!!!
        
        # entregar la informacion a la plantilla
        data.append({
            "nombre": nombre,
            "email": email,
            "telefono": celular, 
            "region": region, 
            "comuna": comuna, 
            "dispositivo": nombre_disp,
            "descr": descripcion,
            "tipo": tipo, 
            "anhos": anhos_uso,
            "estado": estado
        })

    return render_template("html/ver-dispositivos.html", data=data)

@app.route("/confirmar", methods=["POST"])
def confirmarForm():
    name   = request.form.get("username")
    email  = request.form.get("email")
    phone  = request.form.get("phone-number") 
    region = request.form.get("select-region") 
    comuna = request.form.get("select-comuna")

    device  = request.form.get("device-name")
    descrip = request.form.get("device-descr")
    tipo    = request.form.get("device-type")
    anhos   = request.form.get("years-of-use") ##primero validar (como str), hacer strip() y luego pasar a int
    estado  = request.form.get("working-status")
    fotos   = request.files.get("device-pics")

    if validate_user(name, email, phone, region, comuna):
        fecha_creacion = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        db.create_user(name, email, phone, int(comuna), fecha_creacion)
    else:
        error="Hay un error!"
        print(error)
        return render_template("html/agregar-donacion.html",error=error)
    
    devices_info  = request.form.get("device-section")
    i = 1 # revisar cual es el primero
    #while ??? :
    #    i+=1
    #    if validate_device(device, descrip, tipo, anhos, estado, fotos):
            
    
       
    return render_template("html/agregar-donacion.html")


if __name__ == "__main__":
    app.run(debug=True)