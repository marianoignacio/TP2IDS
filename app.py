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
            "informacion_kits":"Uno de los momentos de mayor excitación para un corredor es "
            "el de recibir el kit o bolsa de corredor de la carrera en la que va a participar. "
            "Meses de preparación y entrenamiento se compensan con el ambiente festivo de las ferias de corredores."
            "Allí nos sentimos rodeados de personas que comparten nuestros intereses, nuestros amigos compañeros de corridas, "
            "familiares y sobre todo tenemos la sensación de que el momento tan esperado ya está aquí.",
            "fecha": "24 de Octubre de 2025", 
            "horario": "8am", 
            "lugar": "Tandil, Buenos Aires", 
            "tipo_carrera": "MTB rural", 
            "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "45.000"}, 
                                2: {"nombre": "Larga" ,"valor": "60.000"}}, 
            "puntos_de_hidratacion_30": "Intersecciones con las calles: San Martín, Las Heras, Sáenz Peña",
            "puntos_de_hidratacion_80": "Intersecciones con las calles: San Martín, Las Heras, Sáenz Peña, Franklin, Honduras, Montiel",
            "punto_llegada" : "Azcuénaga 641 (Parque Independencia)",
            "punto_salida" : "Tandil, B7000",
        } 
    ,2:{
            "Auspiciantes": ["Nike","Gatorade", "Villavicencio", "Swiss Medical"],
        }
    ,3:{
          "listado": {1: "- Remera oficial del evento, con diseño exclusivo y materiales transpirables."
                      
                ,1_2: "Remera única por cada participante "

                ,2: "-  Medalla de finalista y de participación, como recuerdo de la competición"

                ,2_2:"Número de competencia + chip de cronometraje"

                ,3:"-  Botella personalizada, posee una tapa de calidad que cierre herméticamente, transparente con el logo de la carrera "

                ,3_2:"Botella de agua: es imprescindible una bebida para todos los participantes"

                ,4:"-   Obsequios de patrocinadores como barras energéticas, geles, snacks de frutos ,semillas secas, avena o granola "

                ,4_2: "Muestras de geles y bebidas energizantes"

                ,5: "-  Muestras de suplementos vitamínicos, además de Seguro de accidentes y cobertura médica básica durante la carrera.  "

                ,5_2:" Artículos para el tratamiento de lesiones como cremas hidratantes, protector solar, vaselina, antiinflamatorios,"

                ,6:"-  Bolso/Bolsa de corredor:un bolso reusable de tela o material impermeable usualmente estampado con el logo de la carrera."

                ,6_2:   "Contiene también los accesorios como cascos y viseras, toallas de algodón o tela de secado rápido. Para que los ciclistas se puedan adaptar comodamente al clima"
                
                ,7:"-  Fotografías profesionales del evento.."

                ,7_2:" Mapa del recorrido."}
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
        archivo=request.form['archivo']
    

        msg = Message(
            subject=f"Inscripcion de: {nombre}",
            recipients=['mtbrally51@gmail.com'], 
            body=f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha de nacimiento: {nacimiento}\nTipo de carrera: {carrera}\nNacionalidad: {nacionalidad}\nMensaje:\n{observaciones}\nFoto:{archivo}"
        )

        mail.send(msg)

    
    except Exception as e:
        print(f"Error enviando mail: {e}") 
        flash("Hubo un error al enviar tu mensaje, intenta más tarde")
    return render_template('index.html', info_evento=diccionario)

if __name__== '__main__':
        app.run("localhost", port=8088, debug=True)
