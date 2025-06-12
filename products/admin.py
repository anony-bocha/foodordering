from django.contrib import admin
from .models import Product, ProductMetaInformation, ProductImages

# Inline to show images inside Product admin
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  # Number of empty forms shown

# Admin for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_slug')
    prepopulated_fields = {'product_slug': ('product_name',)}
    inlines = [ProductImagesInline]

# Admin for Product Meta Information
@admin.register(ProductMetaInformation)
class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_quantity', 'product_measuring', 'is_restrict', 'restrict_quantity')

# Admin for Product Images (only if needed outside the inline)
@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_images', 'created_at')
