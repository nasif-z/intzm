from django.urls import path
from . import views

urlpatterns = [
    path('openai/', views.company_profile_view, name='company_profile_view'),
    path('edit-profile/', views.company_signup, name='company_signup'),
    path('create-post/', views.create_post, name='create_post'),
]