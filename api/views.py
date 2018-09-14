from django.shortcuts import render
from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework import filters

from api.serializers import (StoreSerializer, 
	CategorySerializer,
	OfferSerializer)
from offers.models import (Store,
	Category,
	Offer,
	Deal)

class StoreViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows stores to be viewed or edited.
	"""
	queryset=Store.objects.all()
	serializer_class=StoreSerializer
	filter_backends = ( django_filters.rest_framework.DjangoFilterBackend,)
	search_fields = ('=storeAffName', 'description')
	# ordering_fields = ('storeAffName',)


class CategoryViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows categories to be viewed or edited
	"""
	queryset=Category.objects.all()
	serializer_class=CategorySerializer

class OfferViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows offers to be viewed or edited
	"""
	queryset=Offer.objects.all()
	serializer_class=OfferSerializer