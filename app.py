
from markupsafe import escape
from flask import Flask, abort, render_template, request, flash, url_for, redirect

#instancia  de la aplicación web
app=Flask(__name__, template_folder='templates')
app.secret_key='12345'
#Ruta raíz
@app.route('/')

#Controlador quer renderiza la página principal
def index():
    return render_template('index.html')


nllamadas=[]
placas=[]
fechas=[]
horas=[]


#Ruta enviar
@app.route('/enviar', methods=['POST'])

#Controlador quer renderiza la página principal
def enviar():
    """ Funcion que predice si puede circular o no """
    llamada=request.form.get('numero_llamada')
    placa=request.form.get('placa')
    fecha=request.form.get('fecha')
    hora=request.form.get('hora')

    nllamadas.append(llamada)
    placas.append(placa)
    fechas.append(fecha)
    horas.append(hora)

    return render_template('index.html', nllamadas=nllamadas, placas=placas, fechas=fechas, horas=horas)



#función principal
if __name__=='__main__':
    app.run(debug=True)