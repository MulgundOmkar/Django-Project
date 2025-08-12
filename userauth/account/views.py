from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('home')
        form.add_error(None, 'Invalid credentials')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def team_updates(request):
    return render(request, 'team_updates.html')

@login_required
def employee_handbook(request):
    return render(request, 'employee_handbook.html')

@login_required
def project_reports(request):
    return render(request, 'project_reports.html')

@login_required
def hiring(request):
    return render(request, 'hiring.html')

@login_required
def annual_report(request):
    return render(request, 'annual.html')

@login_required
def new_services(request):
    return render(request, 'new_services.html')

@login_required
def learn_python(request):
    return render(request, 'learn_python.html')
from django.shortcuts import render

def learn_python(request):
    return render(request, 'learn_python.html')

def python_basics(request):
    return render(request, 'python_basics.html')

def flask_framework(request):
    return render(request, 'flask_framework.html')

def django_framework(request):
    return render(request, 'django_framework.html')

def restful_apis(request):
    return render(request, 'restful_apis.html')

def full_stack_dev(request):
    return render(request, 'full_stack_dev.html')
@login_required
def profile_edit(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()

        user.profile.phone = request.POST.get('phone')
        user.profile.save()

        return redirect('dashboard')
    return render(request, 'profile_edit.html')