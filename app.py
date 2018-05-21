
from flask import Flask
import jinja2
from datetime import datetime
from config import picturelist

app = Flask(__name__)

templateLoader = jinja2.FileSystemLoader(searchpath="static/template/")
templateEnv = jinja2.Environment(loader=templateLoader)

TEMPLATE_FILE = "index.html"
template = templateEnv.get_template(TEMPLATE_FILE)

@app.route('/')
def homepage():
    return template.render(piclist=picturelist) 

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


