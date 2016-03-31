from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_new_book, name='get_new_book'),
]