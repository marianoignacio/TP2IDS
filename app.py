'''from flask import Flask
# obligatorio
from flask import render_template

app = Flask(__name__)

# Necesariio para mostrar contenido en un aplicativo
@app.route('/')
# Punto de entrada
def home():
    opciones={
        'opcion 1':'Opcion uno'
    }
    return render_template('index.html')

if __name__ == '__main__':
    app.run("localhost", port=808)'''

from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__) 
 
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = False 
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' 
app.config['MAIL_PASSWORD'] = 'your-email-password'  
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com' 
 

@app.route('/formulario')
def formulario():
        return render_template('registration.html')

@app.errorhandler(404)
def page_not_found(e):
       mensaje="Error de página"
       return render_template('error.html',msj=mensaje)
 
@app.route('/')
def home ():
    diccionario = { 
    1: {    "nombre": "Rally MTB 2025",  
            "organizador": "Club Social y Deportivo Unidos por el Deporte", 
            "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...", 
            "descripcion_larga": "El evento se va a desarrollar en la ciudad de Tandil en Buenos Aires, organizado por " 
            "nuestro club, el día 24 de Octubre de 2025 a las 8am. Existen dos modalidades corta y "
            "larga,  la  primera  es  de  30km  y  la  segunda  de  80km.  Los  costos  y  auspiciantes  se "
            "encuntran mas abajo", 
            "fecha": "24 de Octubre de 2025", 
            "horario": "8am", 
            "lugar": "Tandil, Buenos Aires", 
            "tipo_carrera": "MTB rural", 
            "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "45.000"}, 
                                2: {"nombre": "Larga" ,"valor": "60.000"}}, 
        } 
    ,2:{
            "Auspiciantes": ["Nike","Gatorade", "Villavicencio", "Swiss Medical"],
        }
    }
    return render_template('index.html', info_evento=diccionario)

if __name__== '__main__':
        app.run("localhost", port=8080, debug=True)
