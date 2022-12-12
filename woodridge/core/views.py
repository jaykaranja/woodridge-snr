from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about-us.html')

def gallery(request):
    return render(request, 'core/gallery.html')
    
def admissions(request):
    return render(request, 'core/admissions.html')

def enquiries(request):
    return render(request, 'core/enquiries.html')