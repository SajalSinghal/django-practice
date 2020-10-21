from django.shortcuts import render

# Create your views here.

def help(req):
    my_dict = {'index_me': 'Please help me through this'}
    return render(req, 'help/help.html', context=my_dict)
