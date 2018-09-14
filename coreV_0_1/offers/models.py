from django.db import models
from django.utils.text import slugify
# Create your models here.

class Store(models.Model):
	storeName=models.CharField(max_length=64, null=True, blank=True)
	storeAffName=models.CharField(max_length=128, default="Cuelinks")
	logoUrl=models.URLField(max_length=1024, null=True, blank=True)
	affUrl=models.URLField(max_length=1024, null=True, blank=True)
	description=models.TextField(null=True, blank=True)

	#Not shold be inlcuded in apis
	payouts=models.TextField(null=True, blank=True)
	categoriesList=models.CharField(max_length=512, null=True, blank=True)

	def __str__(self):
		return self.storeAffName

class Payout(models.Model):
	expirty_date=models.DateTimeField(null=True)
	catTitle=models.CharField(max_length=512)
	payout=models.CharField(max_length=128,null=True)
	store=models.ForeignKey('Store', related_name="store_payouts",on_delete=models.CASCADE)

	def __str(self):
		return self.catTitle

class Category(models.Model):
	categoryName=models.CharField(max_length=128)
	categorySlugName=models.CharField(max_length=128,null=True, blank=True)
	stores=models.ManyToManyField(Store, related_name="categories",null=True, blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def __str__(self):
		return self.categoryName

class Offer(models.Model):
	STATUS_CHOICES=(
		('0','Expired'),
		('1','Live')
	)
	store=models.ForeignKey(Store, related_name="offers", on_delete=models.CASCADE)
	category=models.ForeignKey(Category, related_name="offers", on_delete=models.CASCADE)
	offerId=models.CharField(max_length=10, default="1",unique=True, primary_key=True)
	offerTitle=models.CharField(max_length=512)
	offerUrl=models.URLField(max_length=2048, default="http://www.cuelinks.com/")
	offerTerms=models.TextField(null=True, blank=True)
	coupounCode=models.CharField(max_length=30, null=True, blank=True)
	offerStatus=models.CharField(max_length=10, default="live", null=True)
	offerStartTime=models.DateTimeField()
	offerEndTime=models.DateTimeField()
	offerImageUrl=models.URLField(max_length=2048,default="http://www.cuelinks.com/")

	"""
	Store and Category Name as it is in offers file
	"""
	categoryName=models.CharField(max_length=128, null=True, blank=True)
	storeName=models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return self.offerTitle


class Deal(models.Model):
	store=models.ForeignKey(Store, related_name="deals", on_delete=models.CASCADE)
	category=models.ForeignKey(Category, related_name="deals", on_delete=models.CASCADE)
	dealTitle=models.CharField(max_length=512)

	def __str__(self):
		return self.dealTitle