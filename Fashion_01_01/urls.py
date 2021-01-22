from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Fashion_Site, name='Fashion_Site'),
    path('', views.Fashion_Site1, name='Fashion_Site1'),
]

"""from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('add', views.add, name='add'),
    path('add1', views.add1, name='add1')
]"""