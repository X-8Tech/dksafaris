from rest_framework import viewsets, status as http_status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import RideRequest
from .serializers import RideRequestSerializer
from rest_framework.permissions import IsAdminUser


    


class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all().order_by('-created_at')
    serializer_class = RideRequestSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update_status', 'accept', 'complete']:
            return [IsAdminUser()]  # only admins can access these
        return []

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        new_status = request.data.get('status')
        valid_statuses = [choice[0] for choice in ride.STATUS_CHOICES]

        if new_status not in valid_statuses:
            return Response(
                {"error": f"Invalid status. Must be one of {valid_statuses}"},
                status=http_status.HTTP_400_BAD_REQUEST
            )

        ride.status = new_status
        ride.save()
        return Response(RideRequestSerializer(ride).data)

    # Compatibility endpoints
    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        ride = self.get_object()
        ride.status = 'accepted'
        ride.save()
        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        ride = self.get_object()
        ride.status = 'completed'
        ride.save()
        return Response({'status': 'completed'})
