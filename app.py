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
import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__) 
 
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)
 
 
 
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
            "puntos_de_hidratacion_30": "Intersecciones con las calles: San Martín, Las Heras, Sáenz Peña",
            "puntos_de_hidratacion_80": "Intersecciones con las calles: San Martín, Las Heras, Sáenz Peña, Franklin, Honduras, Montiel",
            "punto_llegada" : "Azcuénaga 641",
            "punto_salida" : "Tandil, B7000",
        } 
    ,2:{
            "Auspiciantes": ["Nike","Gatorade", "Villavicencio", "Swiss Medical"],
        }
    }

@app.route('/formulario')
def formulario():
        return render_template('registration.html', info_evento=diccionario)

@app.errorhandler(404)
def page_not_found(e):
       mensaje="Error de página"
       return render_template('error.html',msj=mensaje, info_evento=diccionario)
 
@app.route('/')
def home ():
    return render_template('index.html', info_evento=diccionario)
@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        nombre = request.form['nombre']
        apellido= request.form['apellido_pat']
        carrera=request.form['carrera']
        dni= request.form['DNI']
        nacimiento= request.form['nacimiento']
        nacionalidad= request.form['nacionalidad']
        observaciones= request.form['observaciones']
    

        msg = Message(
            subject=f"Inscripcion de: {nombre}",
            recipients=['mtbrally51@gmail.com'], 
            body=f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha de nacimiento: {nacimiento}\nTipo de carrera: {carrera}\nNacionalidad: {nacionalidad}\nMensaje:\n{observaciones}"
        )

        mail.send(msg)

        return "Mensaje enviado correctamente"
    except Exception as e:
        print(f"Error enviando mail: {e}") 
        flash("Hubo un error al enviar tu mensaje, intenta más tarde")

if __name__== '__main__':
        app.run("localhost", port=8080, debug=True)
