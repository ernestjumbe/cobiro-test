from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path


if settings.DATA_SOURCE == "json_file":
    api_urlpatterns = [
        path('stores/',
            include('filestore.urls')),
    ]
else:
    api_urlpatterns = [
        path('stores/',
            include('stores.urls')),
    ]

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'mysite.views.home', name='home'),
    # re_path(r'^blog/', blog.urls),
    path('api/', include(api_urlpatterns)),

    path('admin', admin.site.urls),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
