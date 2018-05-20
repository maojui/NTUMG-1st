
from flask import Flask
from jinja2 import Template
from datetime import datetime

app = Flask(__name__)

template = Template('<h1>Hello {{ name }}!</h1>')

@app.route('/')
def homepage():
    return template.render(name='World')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


