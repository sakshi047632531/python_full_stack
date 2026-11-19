from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table


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


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def form(request):
    if request.method == "POST":
        Student_table.objects.create(
            reg_no=request.POST.get('reg_no'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            marks=request.POST.get('marks'),
            dob=request.POST.get('dob')
        )

        return HttpResponse("Saved Successfully!")

    return render(request, 'student.html')