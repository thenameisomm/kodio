from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import include
from django.contrib import admin   

urlpatterns=[
    path('',views.Homepage, name='Homepage'),
    path('aftlogin/',views.Afterlogin, name='Afterlogin'),
  
    path('repositories/',views.Repositories, name='Repositories'),
    path('library',views.Library, name='Library'),
    path('create/',views.Create, name='Create'),
    path('upload/',views.Upload, name='Upload'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('blog/',views.Blog, name='Blog'),
    path('careers/',views.Careers, name='Careers'),
    path('contact/',views.Contact, name='Contact'),
    path('customers/',views.Customers, name='Customers'),
    path('privacy/',views.Privacy, name='Privacy'),
    path('reviews/',views.Reviews, name='Reviews'),
    path('security/',views.Security, name='Security'),
    path('services/',views.Services, name='Services'),
    path('support/',views.Support, name='Support'),
    path('terms/',views.Terms, name='Terms'),
    path('about/',views.About, name='About'),
        path('update-repository/<int:rep_id>/', views.Update, name='Update_repository'),
 
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('profileform/', views.profileform, name='profileform'),
    path('showprofile/', views.showprofile, name='showprofile'),
    
   path('updateprofile/', views.updateprofile, name='updateprofile'),  
     
 path('accounts/', include('django.contrib.auth.urls')), 
  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)