from .models import Booking, Flight
from rest_framework.generics import ListAPIView 
from flights.models import Flight
from .serializers import FlightListSerializer , BookingsListSerializer

#the serializer is doing here is taking each individual queryset object provided 
# and converting it into JSON format

class ListView(ListAPIView):
    queryset = Flight.objects.all() # read from the database
    serializer_class = FlightListSerializer

class BookingsListView(ListAPIView):
    queryset = Booking.objects.all() 
    serializer_class = BookingsListSerializer