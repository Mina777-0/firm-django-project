from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Department, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView


class PasswordForm(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class Register(UserCreationForm):
    """The fields here can be added or not it's optional. But they should be mentioned in the fields varaible in the nested class"""
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = {"username", "password1", "password2", "first_name", "last_name", "email"}

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('main')

        else:
            return render(request, "firm/log_in.html", {'message': "Invalid Account"})
        
    return render(request, "firm/log_in.html")

@login_required(login_url='log_in')
def main(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('log_in'))
    return render(request, "firm/main.html")

def log_out(request):
    logout(request)
    return render(request, "firm/log_in.html")

def signup(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Register()
    return render(request, "firm/signup.html", {'form': form})


@login_required(login_url='log_in')
def depts(request):
    if request.method == "POST":
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddEmployee()

    return render(request, "firm/depts.html",{'depts': Department.objects.all(), 'form': form})


@login_required(login_url='log_in')
def employees(request, dept_id):
    dept = Department.objects.get(id = dept_id)
    return render(request, "firm/employees.html",{'dept': dept.posts.all()})


@login_required(login_url='log_in')
def password_success(request):
    return render(request, "firm/password_success.html")