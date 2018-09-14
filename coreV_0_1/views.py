from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from coreV_0_1.offer.models import (
		Store,
		Offer,
		Deal,
		Category,
	)
from coreV_0_1.offer.serializers_0_1 import OfferSerializer

class OfferListView(generics.ListCreateAPIView):
	queryset=Offer.objects.all()
	serializer_class=OfferSerializer