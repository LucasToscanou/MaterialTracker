from django.contrib import admin
from django.urls import path
from MaterialTrackerApp import views
from MaterialTrackerApp.models import *
from django.urls.conf import include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from MaterialTrackerSite.views import *
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from rest_framework import routers
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi

schema_view = yasg_schema_view(
    openapi.Info(
        title="API MaterialTracker",
        default_version='v1',
        description="API for materials",
        contact=openapi.Contact(email="lucastoscanop@gmail.com"),
        license=openapi.License(name='GNU GPLv3'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    
    # Access control -------------------------------------------------------------
    # path('accounts/', include('accounts.urls')),
    path('docs/', include_docs_urls(title='Documentação da API')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include(routers.DefaultRouter().urls)),
    path('openapi', get_schema_view(
        title="API material", 
        description="API to fetch material data",), 
        name='openapi-schema'
    ),
    #-----------------------------------------------------------------------------


    path('security/', LoginView.as_view(template_name='security/login.html') , name='sec-login'),
    path('security/register/', views.register , name='register'),
    path('security/logout/', views.logout , name='sec-logout'),
    path('logout/', LogoutView.as_view(next_page = reverse_lazy('sec-login')) , name='logout'),
    path('security/password_change/',
        PasswordChangeView.as_view(
        template_name='security/password_change_form.html', 
        success_url=reverse_lazy('sec-password_change_done'),
        ),
        name='sec-password_change'
    ),
    path('security/password_change_done/',
        PasswordChangeDoneView.as_view(
        template_name='security/password_change_done.html',
        ),
        name='sec-password_change_done'
    ),
    path('security/terminaRegistro/<int:pk>/', 
        MeuUpdateView.as_view(
        template_name='security/user_form.html',
        success_url=reverse_lazy('sec-login'),
        model=User,
        fields=[
        'first_name',
        'last_name',
        'email',
        ],
        ), name='sec-completaDadosUsuario'
    ),
    path('security/addProfilePhoto/<int:pk>/',
        MyAddProfilePhoto.as_view(
        template_name='security/addProfilePhoto.html',
        success_url=reverse_lazy('sec-login'),
        model=UserProfile,
        fields=[
        'avatar',
        ],
        ), name='sec-addProfilePhoto'
    ),

    path('security/password_reset/', PasswordResetView.as_view(
        template_name='security/password_reset_form.html', 
        success_url=reverse_lazy('sec-password_reset_done'),
        html_email_template_name='security/password_reset_email.html',
        subject_template_name='security/password_reset_subject.txt',
        from_email='webmaster@meslin.com.br',
        ), name='password_reset'
    ),
    path('security/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='security/password_reset_done.html',
        ), name='sec-password_reset_done'
    ),
    path('security/password_reset_confirm/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(
        template_name='security/password_reset_confirm.html', 
        success_url=reverse_lazy('sec-password_reset_complete'),
        ), name='password_reset_confirm'
    ),
    path('security/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='security/password_reset_complete.html'
        ), name='sec-password_reset_complete'
    ),
    path('security/user_page', views.userPage, name='sec-user_page'),
    
    path('', include('MaterialTrackerApp.urls')),
    path('accounts/', include('accounts.urls')),
]
