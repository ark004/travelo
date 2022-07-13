from django.http import HttpResponse
from django.shortcuts import render
from. models import place
from. models import news
# Create your views here.
def fun(request):
    l=place.objects.all()
    g=news.objects.all()

    return render(request,"index.html",{'ks':l,'mn':g})

# def hhh(request):
#     g=news.objects.all()

    # return render(request,"index.html",{'mn':g})

def addition(request):
    num1=int(request.GET["num1"])
    num2=int(request.GET["num2"])
    num3=num1+num2
    return render(request,"results.html",{"add":num3})