from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.

def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign Up Sucessful')
            return redirect("users:login")
    
    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)