import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# Ensure a secret key is present so `flash` and sessions work in development
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret_key')

# Configure mail only if MAIL_SERVER is provided to avoid import/startup errors
_mail_server = os.getenv('MAIL_SERVER')
if _mail_server:
    # Use sensible defaults when env vars are missing to prevent crashes
    app.config['MAIL_SERVER'] = _mail_server
    try:
        app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    except (TypeError, ValueError):
        app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    mail = Mail(app)
else:
    # Mail not configured — disable sending but keep the app usable
    mail = None
 
premios =  {1: "Remera oficial del evento, con diseño exclusivo y materiales transpirables."
                      
                ,2: "Remera única por cada participante "

                ,3: "Medalla de finalista y de participación, como recuerdo de la competición"

                ,4:"Número de competencia + chip de cronometraje"

                ,5:"Botella personalizada, posee una tapa de calidad que cierre herméticamente, transparente con el logo de la carrera "

                ,6:"Botella de agua: es imprescindible una bebida para todos los participantes"

                ,7:"Obsequios de patrocinadores como barras energéticas, geles, snacks de frutos ,semillas secas, avena o granola "

                ,8: "Muestras de geles y bebidas energizantes"

                ,9: "Muestras de suplementos vitamínicos, además de Seguro de accidentes y cobertura médica básica durante la carrera.  "

                ,10:" Artículos para el tratamiento de lesiones como cremas hidratantes, protector solar, vaselina, antiinflamatorios,"

                ,11:"Bolso/Bolsa de corredor:un bolso reusable de tela o material impermeable usualmente estampado con el logo de la carrera."

                ,12:   "Contiene también los accesorios como cascos y viseras, toallas de algodón o tela de secado rápido. Para que los ciclistas se puedan adaptar comodamente al clima"
                
                ,13:"Fotografías profesionales del evento.."

                ,14:" Mapa del recorrido."}
 
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
    }

@app.route('/formulario', methods =['GET', 'POST'])
def formulario():
    if request.method == 'POST':    
        nombre = request.form['nombre']
        apellido= request.form['apellido']
        carrera=request.form['carrera']
        dni= request.form['DNI']
        nacimiento= request.form['nacimiento']
        nacionalidad= request.form['nacionalidad']
        mensajes= request.form['mensaje']
        email_usuario = request.form['mail']
    

        msg = Message(
            subject=f"Inscripcion de: {nombre} {apellido}",
            recipients=[email_usuario], 
            body=f"""
            LOS DATOS DE LA INSCRIPCION SON:\n

            Nombre: {nombre}\n
            Apellido:{apellido}\n
            DNI: {dni}\n
            Fecha de nacimiento: {nacimiento}\n
            Tipo de carrera: {carrera}\n
            Nacionalidad: {nacionalidad}\n
            Mensaje:\n
            {mensajes}

            COFIRMAR RECEPCIÓN Y CORROBORAR DATOS, GRACIAS!"""
        )
    try:
        mail.send(msg)

    
    except Exception as e:
        print(f"Error enviando mail: {e}") 
        flash("Hubo un error al enviar tu mensaje, intenta más tarde")
    return render_template('registration.html', info_evento=diccionario)


@app.errorhandler(404)
def page_not_found(e):
       mensaje="Error de página"
       return render_template('error.html',info_evento=diccionario, msj=mensaje),404
 
@app.route('/')
def home ():
    return render_template('index.html', info_evento=diccionario,lista_premios=premios)


if __name__== '__main__':
        app.run("localhost", port=8088, debug=True)
