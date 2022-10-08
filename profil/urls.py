from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/<int:pk>', views.ProfileView.as_view(), name='my_profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
]