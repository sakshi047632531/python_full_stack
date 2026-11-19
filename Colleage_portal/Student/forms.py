from django import forms
from .models import Student_table

class Student_form_data(forms.ModelForm):

    class Meta:
        model = Student_table
        fields = '__all__'