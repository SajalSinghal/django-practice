from django.shortcuts import render

# Create your views here.

def index(req):
    context_dict = {'text': 'Hello World', 'number': 100}
    return render(req, 'basic_app/index.html', context_dict)

def other(req):
    return render(req, 'basic_app/other.html')

def relative(req):
    return render(req, 'basic_app/relative_url_templates.html')
