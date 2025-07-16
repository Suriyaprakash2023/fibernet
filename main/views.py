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
def thankyou(request):
  return render(request,'thank-you.html')


# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Enquiry
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Enquiry
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json

# ✅ Load credentials from environment variable (Render safe)
google_creds = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
credentials = service_account.Credentials.from_service_account_info(
    google_creds,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
service = build('sheets', 'v4', credentials=credentials)

# ✅ Google Sheet settings
SPREADSHEET_ID = '18HRqJv5wETVYUezBczAX4Lrsn3NgtZKL00_oCZbOmUw'
RANGE_NAME = 'Sheet1!A2'  # Use correct tab name!

@csrf_exempt
def enquiry_submit(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            message = request.POST.get('message')

            # ✅ Save to database
            Enquiry.objects.create(name=name, email=email, mobile=mobile, message=message)

            # ✅ Append to Google Sheet
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
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'invalid_method'})
