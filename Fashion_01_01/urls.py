from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.search_page, name='Fashion_Bazaar'),
    url(r'^search_bar/$', views.search_bar_url, name='search_bar_url'),
    url(r'^search_form/$', views.choice_url, name='choice_url'),
]

"""from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('add', views.add, name='add'),
    path('add1', views.add1, name='add1')
]"""