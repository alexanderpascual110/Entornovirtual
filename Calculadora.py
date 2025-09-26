from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = '<h1>¡Hola bienvenido a la calculadora de Flask!</h1>'
    
    mensaje += '<h2>Para poder usarla tendras que hacer lo siguiente</h2>'
    mensaje += '<ol>'
    mensaje += '<li><h2>sumar http://127.0.0.1:5000/sumar/10/20</h2></li>'
    mensaje += '<li><h2>restar http://127.0.0.1:5000/restar/1020</h2></li>'
    mensaje += '<li><h2>multiplicar http://127.0.0.1:5000/multiplicar/1020</h2></li>'
    mensaje += '<li><h2>dividir http://127.0.0.1:5000/dividir/1020</h2></li>'
    mensaje += '<li><h2>maximo http://127.0.0.1:5000/maximo/1020</h2></li>'
    mensaje += '<li><h2>minimo http://127.0.0.1:5000/minimo/1020</h2></li>'
    mensaje += '</ol>'
    return mensaje 


@app.route('/sumar/<v1>/<v2>')
def sumar(v1,v2):
    s = str(float (v1) + float (v2))
    mensaje = f"<h1>La suma de {v1} + {v2} es {s} </h1>"
    return mensaje 

@app.route('/restar/<v1>/<v2>')
def restar(v1,v2):
    s = str(float (v1) - float (v2))
    mensaje = f"<h1>La resta de {v1} - {v2} es {s} </h1>"
    return mensaje 
if __name__ == '__main__':
    app.run(debug=True)