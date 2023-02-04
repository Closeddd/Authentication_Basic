from django.shortcuts import render,redirect
from .models import Accounts
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def homepage(request,*args,**kwargs):
    return render(request,'home.html',{})

def registration_page(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            Accounts.objects.create(username = register_form['username'].value(), password = register_form['password'].value(), email = register_form['email'].value())
            print(register_form['username'].value())
            messages.success(request,('your account has been registered!'))
            
        else:
            print("error")
            messages.error(request,'your account registration has failed')
            
            
        
    
    register_form = RegistrationForm(request.POST or None)
    return render(request,'register.html',context={'register_form':register_form})

