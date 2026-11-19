from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add/', views.form, name='add'),
    path('add_form/', views.Student_form_dj, name='dj_form'),
]