from django.contrib import admin
from .models import Store, Product

class ProductAdminInline(admin.StackedInline):
    model = Product
    extra = 0

class StoreAdmin(admin.ModelAdmin):
    inlines = [ProductAdminInline]

admin.site.register(Store, StoreAdmin)
