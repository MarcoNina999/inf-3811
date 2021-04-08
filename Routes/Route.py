from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola muno!'

@app.route('/parameter/')
@app.route('/parameter/<name>/')
@app.route('/parameter/<name>/<last_name>/')
def parameter(name = 'ROOT', last_name = ' '):
    return 'Hola ( {} {}'.format(name , last_name) + ' ) como se encuentra hoy?'

if __name__ == '__main__':
    app.run(debug = True , port = 5001)