from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from coreV_0_1.offers.models import (
		Store,
		Offer,
		Deal,
		Category,
	)
from coreV_0_1.offers.serializers import (OfferSerializer,
	StoreInfoSerializer,
	StoreOfferListSerializer,

	CategorySerializer,
	CategoryOfferListSerializer,
	CategoryStoreListSerializer,
	)

class OfferListCreateAPIView(generics.ListCreateAPIView):
	queryset=Offer.objects.all()
	serializer_class=OfferSerializer

	def list(self, request):
		queryset=self.get_queryset()
		serializer_data=OfferSerializer(queryset, many=True)
		return Response(serializer_data.data)


class OfferRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset=Offer.objects.all()
	serializer_class=OfferSerializer
	lookup_fields=['pk']


#================================Stores====================================

class StoreListCreateAPIView(generics.ListCreateAPIView):
	queryset=Store.objects.all()
	serializer_class=StoreInfoSerializer

	def list(self, request):
		queryset=self.get_queryset()
		serializer_data=StoreInfoSerializer(queryset, many=True)
		return Response(serializer_data.data)


class StoreRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset=Store.objects.all()
	serializer_class=StoreInfoSerializer
	lookup_fields=['pk']


class StoreOfferListAPIView(generics.RetrieveAPIView):
	queryset=Store.objects.all()
	serializer_class=StoreOfferListSerializer
	lookup_fields=['pk']


#==================================Category================================
class CategoryListAPIView(generics.ListAPIView):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer

	def list(self, request):
		queryset=self.get_queryset()
		serializer_data=CategorySerializer(queryset, many=True)
		return Response(serializer_data.data)

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer
	lookup_fields=['pk']

class CategoryOfferListAPIView(generics.RetrieveAPIView):
	queryset=Category.objects.all()
	serializer_class=CategoryOfferListSerializer
	lookup_fields=['pk']

class CategoryStoreListAPIView(generics.RetrieveAPIView):
	queryset=Category.objects.all()
	serializer_class=CategoryStoreListSerializer
	lookup_fields=['pk']