from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Fashion_Site, name='Fashion_Site'),
    path('Fashion_Site1', views.Fashion_Site1, name='Fashion_Site1'),
    path('Fashion_Site1_URL', views.Fashion_Site1_URL, name='Fashion_Site1_URL'),
    path('Fashion_Site2_URL', views.Fashion_Site2_URL, name='Fashion_Site2_URL'),
    path('Fashion_Site2', views.Fashion_Site2, name='Fashion_Site2'),
]

"""from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('add', views.add, name='add'),
    path('add1', views.add1, name='add1')
]"""