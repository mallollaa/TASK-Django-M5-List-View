from .models import Booking, Flight
from rest_framework.generics import ListAPIView 
from flights.models import Flight
from .serializers import FlightListSerializer , BookingsListSerializer
from django.utils import timezone

#the serializer here is taking each individual queryset object provided 
# and converting it into JSON format

class ListView(ListAPIView):
    queryset = Flight.objects.all() # read from the database
    serializer_class = FlightListSerializer

class BookingsListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt =timezone.now()) # we use filter to chose spisifc feild
    # __gt mean grater than 
    serializer_class = BookingsListSerializer