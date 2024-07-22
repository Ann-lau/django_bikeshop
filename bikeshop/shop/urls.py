from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, bike_list, bike_add, bike_edit, bike_delete

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('bikes/', bike_list, name='bike_list'),
    path('bikes/add/', bike_add, name='bike_add'),
    path('bikes/edit/<int:pk>/', bike_edit, name='bike_edit'),
    path('bikes/delete/<int:pk>/', bike_delete, name='bike_delete'),
    # Add URLs for Customer and Sale views
]

