from django.shortcuts import render,redirect

# Create your views here.
from  django.http import HttpResponse,JsonResponse
from .models import Students


def  render1(request):
       return render(request,"index.html",)
def  redirect1(request):
    return redirect("https://www.djangoproject.com/start/")
def  HttpResponse1(request):
    return HttpResponse("<h1 style='background-color: pink'> heello.3..</h1>")
def  JsonResponse1(request):
    return JsonResponse("<h1 style='background-color: pink'> heello.4..</h1>")

def data(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)

    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('details')
    phone=request.POST.get('phone')
    volume=request.POST.get('volume')
    subscribe=request.POST.get('subscribe')
    dob=request.POST.get('dob')
    gender=request.POST.get('gender')
    resume=request.FILES.get('resume')
    profile_pic=request.FILES.get('profile_pic')
    age=request.POST.get('age')

    print(username,email,detail,profile_pic,age,resume,gender,phone,volume,subscribe)
    Students.objects.create(username=username,email=email,dob=dob,profile_pic=profile_pic,age=age,resume=resume,gender=gender,phone=phone,volume=volume,subscribe=subscribe)
