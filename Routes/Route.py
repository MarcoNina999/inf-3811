from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola muno!'

@app.route('/parameter/<name>/')
def parameter(name):
    return 'Hola ( {}'.format(name) + ' ) como se encuentra hoy?'

if __name__ == '__main__':
    app.run(debug = True , port = 5001)