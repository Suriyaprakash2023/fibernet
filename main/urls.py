
from django.contrib import admin
from django.urls import path,include
from main.views import *
urlpatterns = [
    path('', index,name='index'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('act/', act,name='act'),
    path('airtel/', airtel,name='airtel'),
    path('hathway/', hathway,name='hathway'),
    path('thankyou/', thankyou,name='thankyou'),
    path('submit-enquiry/', enquiry_submit, name='submit-enquiry'),
]
