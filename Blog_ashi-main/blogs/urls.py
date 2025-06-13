from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),
]