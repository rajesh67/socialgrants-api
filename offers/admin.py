from django.contrib import admin
import csv
# Register your models here.
from offers.models import (Category, Store)

from django.http import HttpResponse
# from django.template import register
from offers.models import (
		Store,
		Offer,
		Payout,
		Category,
	)
# Register your models here.


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

# @admin.register(Offer)
class OfferAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display=['offerTitle','store','category','offerStatus']
	actions=['export_as_csv']

class StoreAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display=['storeAffName','affUrl']
	actions=['export_as_csv']

class CategoryAdmin(admin.ModelAdmin,ExportCsvMixin):
	list_display=['categoryName']
	actions=['export_as_csv']

admin.site.register(Offer, OfferAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
