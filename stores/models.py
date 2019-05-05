from django.db import models

class Store(models.Model):

    store_name = models.CharField("store_name", max_length=254)

    def __str__(self):
        return self.store_name


class Product(models.Model):

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField("title", max_length=254)
    link = models.URLField("link", max_length=400, blank=True, null=True)
    description = models.TextField("description")
    image_link = models.URLField("image_link",
        max_length=400, blank=True, null=True)

    def __str__(self):
        return self.title
