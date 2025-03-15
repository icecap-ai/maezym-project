from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer

from django.shortcuts import render

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'maezym/reservation_list.html', {'reservations': reservations})
