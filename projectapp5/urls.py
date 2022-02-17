from importlib.resources import path
from . import views
from django.urls import path

urlpatterns=[
    path('login',views.loginfunction),
    path('grid',views.gridfunction),
    path('page',views.pagefunction),
    path('form',views.formfunction),
    path('carousel',views.carouselfunction),
    path('modal',views.modalfunction),
]