from django.shortcuts import render, redirect
from .models import TourRequests, Enquiries, Applications

# Create your views here.

def index(request):
    if request.method == "POST":
        rq = TourRequests.objects.create()
        rq.full_names = request.POST['fullname']
        rq.phone_number = request.POST['phonenumber']
        rq.student_name = request.POST['studentname']
        rq.save()
        context = {
            'messagetype' : 'success',
            'message' : 'Your request has been received. We will get in touch with you.'
        }

        return render(request, 'core/index.html', context)

    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about-us.html')

def gallery(request):
    return render(request, 'core/gallery.html')
    
def admissions(request):
    if request.method == "POST":
        rq = Applications.objects.create()
        rq.student_first_name = request.POST['sfn']
        rq.student_second_name = request.POST['ssn']
        rq.student_class = request.POST['sclass']
        rq.kin_first_name = request.POST['kfn']
        rq.kin_surname = request.POST['kinsurname']
        rq.phone_number = request.POST['phone']
        if request.POST['condition'] == "Yes":     
            rq.any_med_condition = True
        else:
            rq.any_med_condition = False

        rq.residence = request.POST['residence']
        rq.save()
        context = {
            'messagetype' : 'success',
            'message' : 'Your application has been received. We will get in touch with you with feedback as soon as possible.'
        }

        return render(request, 'core/admissions.html', context)

    return render(request, 'core/admissions.html')

def enquiries(request):
    if request.method == "POST":
        rq = Enquiries.objects.create()
        rq.names = request.POST['names']
        rq.phone_number = request.POST['phonenumber']
        rq.query = request.POST['query']
        rq.save()
        context = {
            'messagetype' : 'success',
            'message' : 'Your query has been received. We will get in touch with you with an answer as soon as possible.'
        }

        return render(request, 'core/enquiries.html', context)

    return render(request, 'core/enquiries.html')
