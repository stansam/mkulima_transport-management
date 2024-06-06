from django.urls import path
from .views import *



urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # Driver URLs
    path('drivers/', DriverListView.as_view(), name='driver-list'),
    path('drivers/create/', DriverCreateView.as_view(), name='driver-create'),
    path('drivers/<int:pk>/update/', DriverUpdateView.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver-delete'),

    # Vehicle URLs
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),

    # Farmer URLs
    path('farmers/', FarmerListView.as_view(), name='farmer-list'),
    path('farmers/create/', FarmerCreateView.as_view(), name='farmer-create'),
    path('farmers/<int:pk>/update/', FarmerUpdateView.as_view(), name='farmer-update'),
    path('farmers/<int:pk>/delete/', FarmerDeleteView.as_view(), name='farmer-delete'),

    # Job URLs
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/create/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),

    # Revenue URLs
    path('revenues/', RevenueListView.as_view(), name='revenue-list'),
    path('revenues/create/', RevenueCreateView.as_view(), name='revenue-create'),
    path('revenues/<int:pk>/update/', RevenueUpdateView.as_view(), name='revenue-update'),
    path('revenues/<int:pk>/delete/', RevenueDeleteView.as_view(), name='revenue-delete'),
]