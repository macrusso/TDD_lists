from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/delete$', views.delete_list, name='delete_list'),
    url(r'^(\d+)/items/(\d+)/delete/$', views.delete_item, name='delete_item')
]