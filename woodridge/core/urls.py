from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about-us'),
    path('gallery', views.gallery, name='gallery'),
    path('admissions', views.admissions, name='admissions'),
    path('enquiries', views.enquiries, name='enquiries'),

]
