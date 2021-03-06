from django.urls import path, re_path
from .views import ListStores, ListStoreProducts


urlpatterns = [
    re_path(r'^$', ListStores.as_view()),
    re_path(r'^(?P<store_slug>[\w-]+)/$', ListStoreProducts.as_view()),
]
