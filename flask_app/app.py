from flask import Flask, request, render_template, redirect, url_for, session

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

@app.route("/confirmar", methods=("GET", "POST"))
def confirmarForm():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone-number"]
        region = request.form["select-region"]
        comuna = request.form["select-comuna"]

        device = request.form["device-name"]
        descripcion = request.form["device-descr"]
        tipo = request.form["device-type"]
        anhos = request.form["years-of-use"]
        estado = request.form["working-status"]
        fotos = request.form["device-pics"]

        
    return

if __name__ == "__main__":
    app.run(debug=True)