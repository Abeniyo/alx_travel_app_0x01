from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from listings!")

from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
