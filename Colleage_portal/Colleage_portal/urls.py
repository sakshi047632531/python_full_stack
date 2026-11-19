
from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('add/', views.add, name='add'),
    path('add_form/', views.add_form, name='add_form'),

    path('display/', views.display_students, name='display'),

    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
