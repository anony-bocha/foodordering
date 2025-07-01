from django.db import models
import uuid


# Abstract BaseModel
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Product Model
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


# Meta Info
class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="meta_info"
    )
    quantity = models.CharField(null=True, blank=True)
    product_measuring = models.CharField(
        max_length=100,
        null=True,
        choices=(("KG", "KG"), ("ML", "ML"), ("L", "L"), (None, None)),
    )
    product_quantity = models.CharField(null=True, blank=True)
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()


# Product Images
class ProductImages(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    product_images = models.ImageField(upload_to="products/", blank=True, null=True)
