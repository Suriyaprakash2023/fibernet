from django.shortcuts import render,redirect

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



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Enquiry


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

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'invalid_method'})

from django.contrib.auth import authenticate, login
from django.contrib import messages
def login_view(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = authenticate(request,username=username,password=password)
      if user is not None:
            login(request, user)
            return redirect('dashboard')  # Change to your home page URL name
      else:
            messages.error(request, 'Invalid credentials')
   return render(request,'admin/login.html')

def dashboard(request):
  enquiries = Enquiry.objects.all().order_by("-created_at")

  return render(request,'admin/data.html',{"enquiries":enquiries} )



def status_update(request,id):
   if request.method == 'POST':
      status = request.POST['status']
      print(status)

      if status == 'True':
           print("dfd")
           enquiry = Enquiry.objects.get(id=id)
           enquiry.is_enquiryed = True
           enquiry.save()
           
           messages.success(request, 'Status Update successfully')
           return redirect('dashboard')
      else:
          enquiry = Enquiry.objects.get(id=id)
          enquiry.is_enquiryed = False
          enquiry.save()
          messages.success(request, 'Status Update successfully')
          return redirect('dashboard')
            
   return render(request,'admin/login.html')