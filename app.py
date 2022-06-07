
from markupsafe import escape
from flask import Flask, abort, render_template, request, flash, url_for, redirect
from APIHoliday import __is_holiday
from holidayEcuador import HolidayEcuador

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
predicciones=[]


#Ruta enviar
@app.route('/enviar', methods=['POST'])

#Controlador que envia los valores a la tabla
def enviar():
    """ Por medio de esta funcion se pasan los valores del formulario a la tabla"""
    llamada=request.form.get('numero_llamada')
    placa=request.form.get('placa')
    fecha=request.form.get('fecha')
    hora=request.form.get('hora')


    nllamadas.append(llamada)
    placas.append(placa)
    fechas.append(fecha)
    horas.append(hora)
    prediccion=""

    if __is_holiday(self,fecha, True)==True:
        prediccion="T"
        predicciones.append(prediccion)
        return render_template('index.html', nllamadas=nllamadas, placas=placas, fechas=fechas, horas=horas, predicciones=predicciones)
    else:
        prediccion="NT"
        predicciones.append(prediccion)
        return render_template('index.html', nllamadas=nllamadas, placas=placas, fechas=fechas, horas=horas, predicciones=predicciones)
    

    

#Ruta borrar
@app.route('/borrar', methods=['POST'])

#Controlador para borrar la tabla
def borrar():
    """ Funcion que permite borrar la tabla"""
   
    nllamadas.clear()
    placas.clear()
    fechas.clear()
    horas.clear()

    return render_template('index.html', nllamadas=nllamadas, placas=placas, fechas=fechas, horas=horas)


#función principal
if __name__=='__main__':
    app.run(debug=True)