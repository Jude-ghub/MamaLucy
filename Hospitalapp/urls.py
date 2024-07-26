
from django.contrib import admin
from django.urls import path
from Hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('departments/', views.departments, name='departments'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('services/', views.services, name='services'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('patient/', views.patient, name='patient'),





]
