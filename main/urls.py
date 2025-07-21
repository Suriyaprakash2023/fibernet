
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
    path('login_view/', login_view,name='login_view'),
    path('dashboard/', dashboard,name='dashboard'),
    path('submit-enquiry/', enquiry_submit, name='submit-enquiry'),
    path('status_update/<str:id>/', status_update, name='status_update'),
     path('logout_view/', logout_view, name='logout_view'),
]
