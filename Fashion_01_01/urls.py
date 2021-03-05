from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Fashion_Site, name='Fashion_Site'),
    path('Fashion_Site1', views.Fashion_Site1, name='Fashion_Site1'),
    path('Fashion_Site1_URL', views.Fashion_Site1_URL, name='Fashion_Site1_URL'),
    path('Search_Bar_Site2', views.Search_Bar_Site2, name='Fashion_Site2_URL'),
    path('Choice_Bar_Site2', views.Choice_Bar_Site2, name='Choice_Bar_Site2'),
    path('Fashion_Site2', views.Fashion_Site2, name='Fashion_Site2'),
    path('Fashion_Site3', views.Fashion_Site3, name='Fashion_Site3'),
    url(r'^search_bar/$', views.search_bar_url, name='search_bar_url'),
    url(r'^search_form/$', views.choice_url, name='choice_url'),
    url(r'^results/$', views.url_pass_myntra, name='url_pass'),
]

"""from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('add', views.add, name='add'),
    path('add1', views.add1, name='add1')
]"""