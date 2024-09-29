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

if __name__ == "__main__":
    app.run(debug=True)