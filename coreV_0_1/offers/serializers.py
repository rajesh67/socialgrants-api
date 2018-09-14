from rest_framework import serializers

from coreV_0_1.offers.models import (
		Store,
		Category,
		Offer,
		Payout,
	)
# ======================Offers=================================================

class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model=Offer
		fields=('pk','categoryName','storeName','offerId','offerTitle','offerUrl','offerTerms','coupounCode','offerStatus','offerStartTime','offerEndTime','offerImageUrl')

	def create(self, validated_data):
		store,created=Store.objects.get_or_create(storeAffName=validated_data.get('storeName'))
		category,new=Category.objects.get_or_create(categoryName=validated_data.get('categoryName'))
		category.stores.add(store)
		category.save()
		return Offer.objects.create(store=store,category=category,**validated_data)

# ======================Stores==================================================

class StoreInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Store
		fields=('pk','storeName','storeAffName','logoUrl','affUrl','description','payouts','categoriesList')

	def create(self, validated_data):
		store, created=Store.objects.get_or_create(storeAffName=validated_data.get('storeAffName'))
		#update the information
		store.logoUrl=validated_data.get('logoUrl')
		store.affUrl=validated_data.get('affUrl')
		store.description=validated_data.get('description')
		store.payouts=validated_data.get('payouts')
		store.categoriesList=categoriesData
		categoriesData=validated_data.pop('categoriesList')

		categoriesList=categoriesData.split(",")
		for categoryName in categoriesList:
			category, new=Category.objects.get_or_create(categoryName=categoryName.strip())
			store.categories.add(category)
		store.save()
		return store

class StoreOfferListSerializer(serializers.ModelSerializer):
	offers=OfferSerializer(many=True,read_only=True)
	class Meta:
		model=Store
		fields=('pk','storeName','storeAffName','logoUrl','affUrl','description')


# ======================Categories==============================================

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields=('pk','categoryName','categorySlugName')


class CategoryOfferListSerializer(serializers.ModelSerializer):
	offers=OfferSerializer(many=True, read_only=True)
	class Meta:
		model=Category
		fields=('pk','categoryName','categorySlugName','offers')

class CategoryStoreListSerializer(serializers.ModelSerializer):
	stores=StoreInfoSerializer(many=True, read_only=True)
	class Meta:
		model=Category
		fields=('pk','categoryName','categorySlugName','stores')