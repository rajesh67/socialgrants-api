from offers.models import (
	Payout,
	Store,
	Category,
	Offer,
	Deal)

from rest_framework import serializers
from datetime import datetime


class PayoutSerializer(serializers.ModelSerializer):
	class Meta:
		model=Payout
		fields=('pk','expirty_date', 'catTitle', 'payout')

class OfferSerializer(serializers.ModelSerializer):
	# category=serializers.HyperlinkedRelatedField(read_only=True,view_name='category-detail')
	# store=serializers.HyperlinkedRelatedField(read_only=True,view_name='store-detail')
	class Meta:
		model=Offer
		fields=('pk','categoryName','storeName','offerId','offerTitle','offerUrl','offerTerms','coupounCode','offerStatus','offerStartTime','offerEndTime','offerImageUrl')

	def create(self, validated_data):
		store,created=Store.objects.get_or_create(storeAffName=validated_data.get('storeName'))
		category,new=Category.objects.get_or_create(categoryName=validated_data.get('categoryName'))
		category.stores.add(store)
		category.save()
		# print(validated_data)
		return Offer.objects.create(store=store,category=category,**validated_data)

class StoreSerializer(serializers.HyperlinkedModelSerializer):
	# offers=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='offer-detail')
	# categories=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='category-detail')
	offers=OfferSerializer(many=True, read_only=True)
	class Meta:
		model=Store
		fields=('pk','storeName','storeAffName','logoUrl','affUrl','description','payouts','categoriesList','offers')

	def create(self, validated_data):
		categoriesData=validated_data.pop('categoriesList')
		print(categoriesData)
		store, created=Store.objects.get_or_create(storeAffName=validated_data.get('storeAffName'))
		#update the information
		store.logoUrl=validated_data.get('logoUrl')
		store.affUrl=validated_data.get('affUrl')
		store.description=validated_data.get('description')
		store.payouts=validated_data.get('payouts')
		store.categoriesList=categoriesData
		#Add Categories
		categoriesList=categoriesData.split(",")
		for categoryName in categoriesList:
			category, new=Category.objects.get_or_create(categoryName=categoryName.strip())
			store.categories.add(category)
		#save store
		store.save()
		return store

class CategorySerializer(serializers.ModelSerializer):
	# offers=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='offer-detail')
	# stores=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='store-detail')
	# stores=StoreSerializer(read_only=True, many=True)
	offers=OfferSerializer(read_only=True, many=True)
	class Meta:
		model=Category
		fields=('pk','categoryName','offers')