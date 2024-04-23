from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from forms import bookform


# Create your views her
def homepage(request):

    return render(request,'homepage.html')
def aboutpg(request):
    return render(request,'about.html')

def dep(request):
    return render(request, 'department.html')

def doctor(request):
 return render(request, 'doctors.html')

def bookingfn(request):

    if request.method == 'POST':
        Patient_name = request.POST.get('Patient_name')
        Phone_number = request.POST.get('Phone_number')
        Email_id = request.POST.get('Email_id')
        Doctor_name = request.POST.get('Doctor_name')
        Booking_date = request.POST.get('Booking_date')
        Booked_on = request.POST.get('Booked_on')
        user1 = User.objects.create_user(Patient_name=Patient_name,Phone_number=Phone_number,Email_id=Email_id,Doctor_name=Doctor_name,Booking_date=Booking_date,Booked_on=Booked_on)

        user1.save()
    return render(request, 'booking.html')


def newpg(request):
    f = bookform()
    if request.method == "POST":
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page1')

    d2 = {'pip': f}
    return render(request,'book.html',d2)


