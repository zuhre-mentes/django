from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home, login_page, registration_page, second_page, city_detail

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("cities", views.home),
    path('login/', views.login_page, name='login'),# views.py'deki login_page fonksiyonuna yönlendirme yapın
    path('registration/', views.registration_page, name='registration'),
    path('second/', views.second_page, name='second'),
    path('city/<str:city_name>/', views.city_detail, name='city_detail'),
]

from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
