from crypt import methods
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

#Ruta enviar
@app.route('/enviar', methods=['POST'])



#Controlador quer renderiza la página principal
def enviar():
    """ Funcion que predice si puede circular o no """
    return render_template('index.html')



#función principal
if __name__=='__main__':
    app.run(debug=True)