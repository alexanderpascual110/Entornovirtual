from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = '<h1>¡Esta es mi primer pagina!</h1>'
    
    mensaje += '<h2>Visita estos links</h2>'
    mensaje += '<ol>'
    mensaje += '<li><h2>datos http://127.0.0.1:5000/sumar/datos</h2></li>'
    mensaje += '<li><h2>tema1 http://127.0.0.1:5000/restar/tema1</h2></li>'
    mensaje += '<li><h2>tema2http://127.0.0.1:5000/multiplicar/tema2</h2></li>'

    mensaje += '</ol>'
    return mensaje 



if __name__ == '__main__':
    app.run(debug=True)