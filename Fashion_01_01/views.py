# Create your views here.
from django.shortcuts import render
#from .models import destination
from django.http import HttpResponse

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
import random


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
    Url1='https://www.westside.com/collections/'+gender+'-t-shirt?pf_t_size='+size+'&pf_t_brands='+brand
    return render(request,'Fashion_Site1_URL.html', {'URL1':Url1})

def Fashion_Site2(request):
    return render(request,'Fashion_Site2.html')

def Fashion_Site2_URL(request):
    gender=request.GET['gender']
    size=request.GET['size']
    brand=request.GET['brand']
    color=request.GET['color']

    opts = webdriver.ChromeOptions()
    opts.headless = True
    browser = webdriver.Chrome(options=opts)

    """if(brand != 'Any' or color == 'Any'):
        Url2 = 'https://www.pantaloons.com/c/'+gender+'/t-shirts-188?source=menu&page=1&orderway=desc&orderby=position&fp[]=Sizes__fq:'+size+'%7CSubbrand__fq:'+brand+'&utm_campaign=pure_brand_exact_ao&utm_medium=cpc'
        #return render(request, 'Fashion_Site2_URL.html', {'Links2': links})

    elif (brand == 'Any' or color != 'Any'):
        Url2 = 'https://www.pantaloons.com/c/' + gender + '/t-shirts-188?source=menu&page=1&orderway=desc&orderby=position&fp[]=Sizes__fq:' + size + '%7CColor__fq:' + color + '&utm_campaign=pure_brand_exact_ao&utm_medium=cpc'
        return render(request, 'Fashion_Site2_URL.html', {'URL2': Url2})"""

    Url2='https://www.pantaloons.com/c/'+gender+'/t-shirts-188?source=menu&page=1&orderway=desc&orderby=position&fp[]=Color__fq:'+color+'%7CSizes__fq:'+size+'%7CSubbrand__fq:'+brand+'&utm_campaign=pure_brand_exact_ao&utm_medium=cpc'
    browser.get(Url2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    re1 = soup.find('div', class_="container-fluid scroll_head_top")
    re2 = re1.find('div', class_='row')
    re3 = re2.find('div', attrs={'class': 'col-lg-9 col-md-9 col-sm-8 col-xs-9 category-list-view'})
    re4 = re3.find('div', attrs={'class': 'filter_content_wrapper'})
    re_best = re4.find('div', {'class': 'product_search_content row'})

    links = []
    for one_set in re_best.find_all("div", class_="col-lg-4 col-md-4 col-sm-4 col-xs-4 category-list-col"):
        a1 = one_set.find("li", class_='slide')
        if a1:
            a2 = a1.find("a")
        if a2:
            links.append(a2.get('href'))
    #print(links)
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)
    # browser.get(links[0])
    return render(request,'Fashion_Site2_URL.html', {'Links2': links, 'Url2': Url2},)







def Fashion_Site3(request):
    return render(request,'Fashion_Site3.html')


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
