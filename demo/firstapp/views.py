from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# Create your views here.
@login_required(login_url="login_view")
def home(request):
    emp = Employee.objects.all()
    return render(request, "home.html", {"emp": emp})


def add_employee(request):
    if request.method == "POST":
        enrl = request.POST.get("empid")
        empName = request.POST.get("empName")
        empPassword = request.POST.get("empPassword")
        empEmail = request.POST.get("empEmail")
        empAddress = request.POST.get("empAdd")
        empMo = request.POST.get("empMo")
        print("emp name is:", empName)
        print("emp email is:", empEmail)
        data = Employee.objects.create(
            roll=enrl, name=empName, email=empEmail, address=empAddress, contact=empMo
        )
        if data:
            print("Data Added")
            return redirect("homepage")
    try:
        last_record = Employee.objects.latest("roll")
        if last_record:
            last_id = last_record.roll
        else:
            last_id = 0
    except:
        last_id = 0
    return render(request, "add.html", {"roll": last_id + 1})


def delete(request, roll):
  try:
    del_emp = Employee.objects.get(pk=roll)
    del_emp.delete()
    return redirect("homepage")
  except:
     return render(request, "home.html", {"error": "Invalid credentials"})


def update(request, roll):
  try:
    emp = Employee.objects.get(pk=roll)
    return render(request, "update.html", {"emp": emp})
  except:
     return render(request, "home.html", {"error": "Invalid credentials"})


def do_update(request, roll):
    enrl = request.POST.get("empid")
    empName = request.POST.get("empName")
    empEmail = request.POST.get("empEmail")
    empAddress = request.POST.get("empAdd")
    empMo = request.POST.get("empMo")

    emp = Employee.objects.get(id=roll)

    emp.roll = enrl
    emp.username = empName
    emp.email = empEmail
    emp.address = empAddress
    emp.contact = empMo

    emp.save()
    return redirect("homepage")


def add_user(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            empName = form.cleaned_data["username"]
            empPassword = form.cleaned_data["password"]
            empEmail = form.cleaned_data["email"]
            empAddress = form.cleaned_data["address"]
            empContact = form.cleaned_data["contact"]
            emproll = form.cleaned_data["roll"]

            # Create a new User instance
            user = User.objects.create(
                username=empName,
                email=empEmail
                # password=empPassword
            )
            if user:
                user.set_password(empPassword)
                user.save()

            # Create a new Employee instance linked to the User
            Employee.objects.create(
                user=user,
                roll=emproll,
                username=empName,
                password=empPassword,
                email=empEmail,
                address=empAddress,
                contact=empContact,
            )

            return redirect("homepage")
    else:
        form = EmployeeForm()

    return render(request, "add_employee.html", {"form": form})


# Login Functionality using Defined model in models.py
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("inside if condition of is_valid method")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    else:

        return render(request, "login.html")


@login_required(login_url="login_view")
def logout_view(request):
    logout(request)
    return redirect("login_view")


# Class based view
class MyView(View):
    name = "Unknown"

    def get(self, request):
        return HttpResponse(self.name)


# Render on any page using class based view
class PageRender(View):
    def get(self, request):
        return render(request, "add_employee.html")


# Render on any page using class based view with context
class ContextPage(View):
    def get(self, request):
        context = {"message": "Class based view with context what about new challenges"}
        return render(request, "add_employee.html", context)


# Class based login view
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "add_employee.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Data submittd successfully")
