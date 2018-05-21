
from flask import Flask
from jinja2 import Template
from datetime import datetime

app = Flask(__name__)

template = Template('<img src="static/images/{{ block.profile_image }}" alt={{ block.name }} width="120" height="120" />')

@app.route('/')
def homepage():
    return template.render(block={'profile_image':'1-1.jpg','name':
    'haha'})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


