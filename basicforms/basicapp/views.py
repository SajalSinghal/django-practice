from django.shortcuts import render
from . import forms
# Create your views here.

def index(req):
    return render(req, 'basicapp/index.html')

def form_name_view(req):
    form = forms.FormName()

    if req.method == 'POST':
        form = forms.FormName(req.POST)

        if form.is_valid():
            print('Validation Success!')

            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])

    return render(req, 'basicapp/form_page.html', {'form': form})
