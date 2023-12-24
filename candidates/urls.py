from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/edit-profile/', views.edit_profile, name='edit_profile'),
    path('<str:pk>/', views.view_profile, name='view_profile'),
    path('dashboard/applied-internships/', views.applied_internships, name='applied_internships'),
    path('dashboard/saved-internships/', views.saved_internships, name='saved_internships'),
    path('dashboard/messages/', views.messaging, name='messaging'),
    path('dashboard/book-interview/', views.book_interview, name='book_interview'),
]