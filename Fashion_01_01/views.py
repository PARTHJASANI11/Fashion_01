# Create your views here.
from django.shortcuts import render
#from .models import destination
from django.http import HttpResponse


# Create your views here.


def Fashion_Site(request):
    #val1 = request.POST['Fashion_Site1']
    return render(request, 'Fashion_Site.html')

def Fashion_Site1(request):
    return render(request,'Fashion_Site1.html')

def Fashion_Site1_URL(request):
    gender=request.GET['gender']
    size=request.GET['size']
    brand=request.GET['brand']
    Url='https://www.westside.com/collections/'+gender+'-t-shirt?pf_t_size='+size+'&pf_t_brands='+brand
    return render(request,'Fashion_Site1_URL.html', {'URL':Url})


""" from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

#def home(request):
 #   return HttpResponse('Hello! I am Parth Jasani. I am ready to learn Django.')

def home1(request):
    #return HttpResponse('Hello! I am home1.')
    # return render(request,'hello1.html')
    #i = input("Enter Your Name:")
    return render(request,'hello1.html',{'name':'Parth'})

def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2
    return render(request,'result.html',{'result': result})

def add1(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result1 = val1 + val2
    return render(request,'result.html',{'result1': result1})

def page(request):
    dest1 = destination()
    dest1.name = 'Mumbai'
    return render(request,'index.html', {'dest1': dest1})
"""
# Create your views here.
