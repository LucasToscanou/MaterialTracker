from django.contrib import admin
from django.urls import path
from MaterialTrackerApp import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'MaterialTrackerApp'


urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_item_success/', views.add_item_success, name='add_item_success'),
    path('add_item_fail/', views.add_item_fail, name='add_item_fail'),
    path('edit_item/<int:pk>', views.edit_item, name='edit_item'),
    path('new_request_view/', views.new_request_view, name='new_request_view'),
    path('new_request_finish/', views.new_request_finish, name='new_request_finish'),
    path('new_request_result/', views.new_request_result, name='new_request_result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
