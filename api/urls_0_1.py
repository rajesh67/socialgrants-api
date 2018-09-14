from django.conf.urls import url, include
from coreV_0_1.offers.views import (OfferListCreateAPIView, 
	OfferRetrieveUpdateAPIView,
	#Stores
	StoreListCreateAPIView,
	StoreRetrieveUpdateAPIView,
	StoreOfferListAPIView,

	#Categories
	CategoryListAPIView,
	CategoryRetrieveAPIView,
	CategoryOfferListAPIView,
	CategoryStoreListAPIView
	)
from coreV_0_1.offers.serializers import (OfferSerializer,
	StoreInfoSerializer,
	StoreOfferListSerializer,

	CategorySerializer,
	CategoryOfferListSerializer,
	CategoryStoreListSerializer,
	)
from coreV_0_1.offers.models import (
		Offer,
		Store,
		Category,
	)

urlpatterns=[
	#Offer List,Update and Details
	url(r'^offers/$',OfferListCreateAPIView.as_view(queryset=Offer.objects.all(), serializer_class=OfferSerializer),name="offer-list"),
	url(r'^offers/(?P<pk>\d+)/', OfferRetrieveUpdateAPIView.as_view(queryset=Offer.objects.all(), serializer_class=OfferSerializer), name="offer-detail"),

	#Store List, Update, Details View
	url(r'^stores/$',	StoreListCreateAPIView.as_view(queryset=Store.objects.all(), serializer_class=StoreInfoSerializer),name="store-list"),
	url(r'^stores/(?P<pk>\d+)/$', StoreRetrieveUpdateAPIView.as_view(queryset=Store.objects.all(), serializer_class=StoreInfoSerializer), name="store-detail"),
	url(r'^stores/(?P<pk>\d+)/offers/$', StoreOfferListAPIView.as_view(queryset=Store.objects.all(), serializer_class=StoreOfferListSerializer), name="store-offer-list"),

	#Category List, OfferList, StoreList
	url(r'^categories/$', CategoryListAPIView.as_view(queryset=Category.objects.all(), serializer_class=CategorySerializer),name='category-list'),
	url(r'^categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(queryset=Category.objects.all(), serializer_class=CategorySerializer),name='category-detail'),
	url(r'^categories/(?P<pk>\d+)/offers/$', CategoryOfferListAPIView.as_view(queryset=Category.objects.all(), serializer_class=CategoryOfferListSerializer),name='category-offer-list'),
	url(r'^categories/(?P<pk>\d+)/stores/$', CategoryStoreListAPIView.as_view(queryset=Category.objects.all(), serializer_class=CategoryStoreListSerializer), name='category-store-list'),
]