from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

# def index(req):
#     my_dict = {'insert_me': "Hello i am from view.py"}
#     return render(req, 'first_app/index.html', context=my_dict)

def index(req):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(req, 'first_app/index.html', context=date_dict)
