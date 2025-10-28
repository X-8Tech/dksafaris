from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, SafariPackage
from .serializers import BookingSerializer, SafariPackageSerializer
from rest_framework.permissions import AllowAny


# 🟢 PUBLIC: List all safari packages
class SafariPackageListView(generics.ListAPIView):
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer
    permission_classes = [AllowAny]


# 🟢 PUBLIC: Create booking
class BookingCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🟠 ADMIN: List + Create Safari Packages
class SafariPackageListCreateView(generics.ListCreateAPIView):
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer
    permission_classes = [permissions.AllowAny]  # You can switch to IsAdminUser later


# 🟠 ADMIN: Retrieve, Update, Delete Safari
class SafariPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer
    permission_classes = [permissions.AllowAny]


# 🟠 ADMIN: View All Bookings
class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all().select_related("safari").order_by("-created_at")
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]
