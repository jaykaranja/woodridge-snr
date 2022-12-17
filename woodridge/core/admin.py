from django.contrib import admin
from .models import TourRequests, Enquiries, Applications, ParentEmails

# Register your models here.

admin.site.register(TourRequests)
admin.site.register(Enquiries)
admin.site.register(Applications)
admin.site.register(ParentEmails)