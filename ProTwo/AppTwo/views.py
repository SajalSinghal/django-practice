from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.

def secondApp(req):
    return HttpResponse('<em>My Second App</em><h1>Welcome!</h1><h2>Go to /users to see the list of users information.</h2>')

def index(req):
    return render(req, 'AppTwo/index.html')

def user(req):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users_records': users_list}
    return render(req, 'AppTwo/AppTwo.html', context=user_dict)

def new_user(req):
    form = NewUserForm()

    if req.method == 'POST':
        form = NewUserForm(req.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(req)

        else:
            print('ERROR FORM INVALID')
            
    return render(req, 'AppTwo/AppTwo.html', {'form': form})
