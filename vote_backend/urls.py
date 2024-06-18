"""
URL configuration for vote_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import LoginTokenView, LoginView
from vote.views import PersonList, MyPersonList , MyPersonDetail
from vote.views.entities import WilayaList, MoughataaList, CommuneList, CentreList, BureauList
from vote.views.entities import WilayaDetail, MoughataaDetail, CommuneDetail, CentreDetail, BureauDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    # show name of the user 

    path('auth/token/', LoginTokenView.as_view(), name="login-token"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path("persons/", PersonList.as_view(), name="pirogue-list"),
    path("my-persons/", MyPersonList.as_view(), name="my-pirogue-list"),
    path("my-persons/<int:pk>/", MyPersonDetail.as_view(), name="my-pirogue-detail"),

    path('wilayas/', WilayaList.as_view(), name='wilaya-list'),
    path('moughataas/', MoughataaList.as_view(), name='moughataa-list'),
    path('communes/', CommuneList.as_view(), name='commune-list'),
    path('centres/', CentreList.as_view(), name='centre-list'),
    path('bureaus/', BureauList.as_view(), name='bureau-list'),

    path('wilayas/<int:pk>/', WilayaDetail.as_view(), name='wilaya-detail'),
    path('moughataas/<int:pk>/', MoughataaDetail.as_view(), name='moughataa-detail'),
    path('communes/<int:pk>/', CommuneDetail.as_view(), name='commune-detail'),
    path('centres/<int:pk>/', CentreDetail.as_view(), name='centre-detail'),
    path('bureaus/<int:pk>/', BureauDetail.as_view(), name='bureau-detail'),
    
    
    
]