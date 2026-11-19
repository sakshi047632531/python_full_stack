from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data


# Home page
def home(request):
    data = {
        'name': 'Neela',
        'age': 20,
        'department': 'BCA'
    }

    marks = [100, 80, 90]

    return render(request, 'home.html', {
        'data': data,
        'marks': marks
    })


# About page
def about(request):
    return render(request, 'about.html')


# Contact page
def contact(request):
    return render(request, 'contact.html')


# Add student using HTML form
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


# Add student using Django ModelForm
def add_form(request):
    if request.method == 'POST':
        form = Student_form_data(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Student Added Successfully!")
    else:
        form = Student_form_data()

    return render(request, 'Student_form_data.html', {'form': form})


# Display students
def display_students(request):
    students = Student_table.objects.all()

    return render(request, 'display_students.html', {
        'students': students
    })