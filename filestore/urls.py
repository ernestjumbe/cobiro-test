from django.urls import path, re_path
from .views import ListStores


urlpatterns = [
    re_path(r'^$', ListStores.as_view()),
]
