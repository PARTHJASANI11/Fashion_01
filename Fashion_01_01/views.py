# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as urllib
import urllib3
import http.cookiejar as cookiejar
import json
import re


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

    images = []
    for one_set in re_best.find_all("div", class_="col-lg-4 col-md-4 col-sm-4 col-xs-4 category-list-col"):
        a1 = one_set.find("div", class_='aspectContainer loadingAnimation')
        if a1:
            a2 = a1.find("img")

        if a2:
            images.append(a2.get('src'))


    #print(links)
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)
    # browser.get(links[0])
    return render(request,'Fashion_Site2_URL.html', {'Links2': links, 'Images2': images},)


def Fashion_Site3(request):
    return render(request, 'Fashion_Site3.html')


def search_bar_url(request):
    if request.method == "POST":
        search_text = request.POST.get('search')
        search_text.lower()
        search_words = search_text.split(' ')
        url = url_pass(search_words)
        links_details_dict = results_collector(url)
        return render(request, "myntra_search_results.html", {"url": url, "links_details_dict": links_details_dict})


def choice_url(request):
    if request.method == "POST":
        inps = ['filter', 'category', 'brand', 'color']
        search_words = []
        for i in inps:
            try:
                search_words.append(request.POST.get(i).lower())
            except AttributeError:
                pass
        url = url_pass(search_words)
        links_details_dict = results_collector(url)
        return render(request, "myntra_search_results.html", {"url": url, "links_details_dict": links_details_dict})


def url_pass(terms):
    search_string = ""
    for i in terms:
        search_string += i
        if i != terms[-1]:
            search_string += "-"
    url = "https://www.myntra.com/" + search_string
    return url


def results_collector(url):
    opts = webdriver.ChromeOptions()
    opts.add_argument('--no-sandbox')
    opts.add_argument("--headless")
    opts.add_argument(
        f'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    xyz = soup.find("div", id="mountRoot")

    links = []
    for one_set in xyz.find_all("li", class_="product-base"):
        a = one_set.find("a")
        if a:
            link = "https://www.myntra.com/" + a.get('href')
            links.append(link)
    hdr = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    links_details_dict = {}
    for site in links:
        http = urllib3.PoolManager()
        req = urllib.Request(site, headers=hdr)

        cj = cookiejar.CookieJar()
        opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))

        response = opener.open(req)
        content = response.read()
        response.close()

        page = BeautifulSoup(content, "html.parser")
        a = page.find_all("script", {"type": "application/ld+json"})
        a = a[1]
        a = json.loads(a.string)
        links_details_dict[site] = [a['image'], a['description'], a['offers']['price']]
    return links_details_dict
