from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')
def about(request):
  return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def act(request):
  return render(request,'act.html')
def airtel(request):
  return render(request,'airtel.html')
def hathway(request):
  return render(request,'hathway.html')


# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Enquiry

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Constants
SERVICE_ACCOUNT_FILE = os.path.join('credentials', 'google_sheet_key.json')  # Update path if needed
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '18HRqJv5wETVYUezBczAX4Lrsn3NgtZKL00_oCZbOmUw'  # Replace with your actual Google Sheet ID
RANGE_NAME = 'Sheet1!A2'  # Adjust if you want a different sheet/range

@csrf_exempt
def enquiry_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        # Save to DB
        Enquiry.objects.create(name=name, email=email, mobile=mobile, message=message)

        # Save to Google Sheet
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=credentials)
        values = [[name, email, mobile, message]]
        body = {'values': values}
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()

        return JsonResponse({'status': 'success'})
