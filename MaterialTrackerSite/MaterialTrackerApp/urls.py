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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_item_success/', views.add_item_success, name='add_item_success'),
    path('add_item_fail/', views.add_item_fail, name='add_item_fail'),
    path('edit_item/<int:pk>', views.edit_item, name='edit_item'),



    path("material/list/", views.MaterialView.as_view(), name='material-list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
