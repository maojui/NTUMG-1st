from japronto import Application
from jinja2 import Template


template = Template('<h1>Hello {{ name }}!</h1>')

def hello(request):
    return request.Response(text=template.render(name='World'), 
                            mime_type='text/html')

app = Application()
app.router.add_route('/', hello)
app.run(port=80,debug=False)
