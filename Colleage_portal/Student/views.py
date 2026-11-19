
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student_table
from .forms import Student_form_data


# 1. HOME PAGE
def home(request):
    data = {
        'name': 'Vaishu',
        'age': 20,
        'department': 'BCA',
    }

    marks = [100, 90, 80]

    return render(request, 'home.html', {
        'data': data,
        'marks': marks
    })


# 2. ABOUT PAGE
def about(request):
    return render(request, 'about.html')


# 3. CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# 4. ADD STUDENT USING HTML FORM
def add(request):
    if request.method == 'POST':
        Student_table.objects.create(
            reg_no=request.POST.get('reg_no'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            marks=request.POST.get('marks'),
            dob=request.POST.get('dob')
        )

        return HttpResponse("Student Added Successfully!")

    return render(request, 'Student_form.html')


# 5. ADD STUDENT USING DJANGO MODEL FORM
def add_form(request):
    if request.method == 'POST':
        form = Student_form_data(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Student Added Successfully!")

    else:
        form = Student_form_data()

    return render(request, 'Student_form_data.html', {
        'form': form
    })


# 6. DISPLAY ALL STUDENTS
def display_students(request):
    students = Student_table.objects.all()

    return render(request, 'display_students.html', {
        'students': students
    })


# 7. USER LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return HttpResponse("Invalid Username or Password")

    return render(request, 'Login.html')


# 8. DASHBOARD
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'Dashboard.html')


# 9. USER LOGOUT
@login_required(login_url='login')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return HttpResponse("Invalid request!")
