from django.contrib import admin
from .models import TourRequests, Enquiries, Applications

# Register your models here.

admin.site.register(TourRequests)
admin.site.register(Enquiries)
admin.site.register(Applications)