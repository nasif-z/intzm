from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('packages/', views.packages, name='packages'),

    path('view-post/<int:id>/', views.view_post, name='view_post'),
    path('all-internships/', views.job_feed, name='job_feed'),
]