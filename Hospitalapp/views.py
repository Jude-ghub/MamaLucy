from django.shortcuts import render,redirect
from Hospitalapp.models import Appointment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def appointment(request):
    if request.method == 'POST':
        appointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        appointments.save()
        return redirect("/show")

    else:
        return render(request, 'appointment.html')


def departments(request):
    return render(request, 'departments.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def services(request):
    return render(request, 'services.html')

def show(request):
    myappointments = Appointment.objects.all()
    return render(request,'show.html',{'appointments': myappointments})

def delete(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect("/show")

def patient(request):
    mypatient = patient.objects.all()
    return render(request,'patients.html',{'patient': mypatient})
