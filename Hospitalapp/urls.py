
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
    path('patients/', views.patient, name='patients'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token')










]
