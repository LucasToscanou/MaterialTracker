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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
