from django.urls import path
from .views import (
    SafariPackageListCreateView,
    SafariPackageDetailView,
    BookingCreateView,
    BookingListView,
)

urlpatterns = [
    # Safari Packages
    path("safaris/", SafariPackageListCreateView.as_view(), name="safari-list-create"),
    path("safaris/<int:pk>/", SafariPackageDetailView.as_view(), name="safari-detail"),

    # User Bookings
    path("bookings/", BookingCreateView.as_view(), name="create-booking"),

    # Admin Bookings (for dashboard)
    path("admin/bookings/", BookingListView.as_view(), name="admin-bookings"),
]
