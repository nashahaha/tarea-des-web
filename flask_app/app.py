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
    return render_template("html/ver-dispositivos.html")

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
        
    return render_template("html/agregar-donacion.html")

if __name__ == "__main__":
    app.run(debug=True)