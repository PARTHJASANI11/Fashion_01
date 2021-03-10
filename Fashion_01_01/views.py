# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as urllib
import urllib3
import http.cookiejar as cookiejar
import json


def search_page(request):
    return render(request, 'search_page.html')


def search_bar_url(request):
    if request.method == "POST":
        search_text = request.POST.get('search')
        if not search_text:
            return render(request, 'search_page.html', {"msg": "Hey! Enter something atleast!"})
        search_text.lower()
        search_words = search_text.split(' ')
        url_myntra = url_pass_myntra(search_words)
        links_details_dict_myntra = results_collector_myntra(url_myntra)
        url_bf = url_pass_bf(search_words)
        links_details_dict_bf = results_collector_bf(url_bf)
        url_pl = url_pass_pl(search_words)
        links_details_dict_pl = results_collector_pl(url_pl)
        all_items = {}
        all_items.update(links_details_dict_bf)
        all_items.update(links_details_dict_myntra)
        all_items.update(links_details_dict_pl)
        return render(request, "myntra_search_results.html", {"all_items": all_items})


def choice_url(request):
    if request.method == "POST":
        inps = ['filter', 'category', 'brand', 'color']
        search_words = []
        for i in inps:
            try:
                search_words.append(request.POST.get(i).lower())
            except AttributeError:
                pass
        if not search_words:
            return render(request, 'search_page.html', {"msg": "Don't simply press submit! First select a radio button!"})
        url_myntra = url_pass_myntra(search_words)
        links_details_dict_myntra = results_collector_myntra(url_myntra)
        url_bf = url_pass_bf(search_words)
        links_details_dict_bf = results_collector_bf(url_bf)
        url_pl = url_pass_pl(search_words)
        links_details_dict_pl = results_collector_pl(url_pl)
        all_items = {}
        all_items.update(links_details_dict_bf)
        all_items.update(links_details_dict_myntra)
        all_items.update(links_details_dict_pl)
        return render(request, "myntra_search_results.html", {"all_items": all_items})


def url_pass_myntra(terms):
    search_string = ""
    for i in terms:
        search_string += i
        if i != terms[-1]:
            search_string += "-"
    url = "https://www.myntra.com/" + search_string
    return url


def results_collector_myntra(url):
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


def url_pass_bf(terms):
    search_string = ""
    for i in terms:
        search_string += i
        if i != terms[-1]:
            search_string += "-"
    url = "https://www.brandfactoryonline.com/" + search_string
    return url


def results_collector_bf(url):
    opts = webdriver.ChromeOptions()
    opts.add_argument('--no-sandbox')
    opts.add_argument("--headless")
    opts.add_argument(
        f'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    xyz = soup.find_all("li", class_="imageView")
    links = []

    for one_set in xyz:
        a = one_set.find("a")
        if a:
            links.append("https://www.brandfactoryonline.com" + a.get('href'))

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
        img = page.find("div", class_="img-thumb slide-selected")
        img = img.find("img")
        img = img.get('src')
        bn = page.find("div", class_="product-brand-name")
        bn = bn.contents[1]
        pn = page.find("div", class_="product-name")
        pn = pn.contents[0]
        price = page.find("div", class_="pd-discount-price")
        if not price:
            price = page.find("div", class_="pd-price-striked")
            if not price:
                price = page.find("span", class_="pd-price")
        if price:
            price = price.contents[0]
            price = price[2:]
        links_details_dict[site] = [img, bn+" "+pn, price]
    return links_details_dict


def url_pass_pl(terms):
    search_string = ""
    for i in terms:
        search_string += i
        if i != terms[-1]:
            search_string += "+"
    url = "https://www.pantaloons.com/c/streamoidsearch?search_query=" + search_string + "&page=1&orderway=desc&orderby=position"
    return url


def results_collector_pl(URL):
    opts = webdriver.ChromeOptions()
    opts.headless = True
    browser = webdriver.Chrome(options=opts)

    browser.get(URL)
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
    di={}
    for i in range(len(links)):
        di[links[i]] = [images[i], "Description", "Price"]

    return di
