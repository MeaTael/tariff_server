from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/orders/$', views.orders_list),
    re_path(r'^api/add/$', views.add_order),
    re_path(r'api/clear/$', views.clear)
]