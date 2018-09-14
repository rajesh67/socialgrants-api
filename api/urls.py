from django.conf.urls import url, include
from rest_framework import routers

from api.views import (StoreViewSet,
	CategoryViewSet,
	OfferViewSet)
#New Urls


router=routers.DefaultRouter()

router.register(r'stores', StoreViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'offers', OfferViewSet)

urlpatterns=[
	url(r'^', include(router.urls)),

	
]