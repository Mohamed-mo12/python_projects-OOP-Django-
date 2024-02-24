from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login , logout as auh_logut
from .forms import RegistrationForm

def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')


    return  render(request,'signup.html',{'form':form})