from django.db import models

class Student_table(models.Model):
    reg_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.DecimalField(max_digits=6, decimal_places=2)
    dob = models.DateField()

    def __str__(self):
        return self.name