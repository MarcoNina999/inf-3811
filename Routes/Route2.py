from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="View")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/parameter/<name>')
def parameter(name):
    return render_template('index.html', _name = name)

if __name__ == '__main__':
    app.run(debug = True, port = 1999)