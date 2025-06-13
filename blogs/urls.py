from django.urls import path
from .views import IndexPage


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]