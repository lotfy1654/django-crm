from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, RecordForm
from .models import Record
# Create your views here.


def home(request):

    records = Record.objects.all()

    if request.user.is_authenticated:
        return render(request, 'home.html', {'records': records})

    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    # Check to see if loggin
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            print("Login successful")
            return redirect('home')
        else:
            messages.error(
                request, "There was an error logging in. Please try again...")
            return redirect('loginurl')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user
            # cleaned data return the valid data from the input fields
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def record_detail(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        custome_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': custome_record})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')
