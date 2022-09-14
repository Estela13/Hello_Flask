from flask import Flask, render_template


app = Flask(__name__)   #variable nombre del fichero

#decorador: función de python para crear la ruta en la que lo vamos a encontrar
@app.route("/hola")
def primeraEntrada():
    return "Hola, mundo"

@app.route("/adios")
def salidad():
    return "Hasta luego Maricarmen"

@app.route("/miprimerhtml")
def primerhtml():
    return render_template("hola.html")