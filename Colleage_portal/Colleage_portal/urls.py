from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student/', views.form, name='add'),
    path('add_form/',views.student_form_dj,name='dj_form'),
]
