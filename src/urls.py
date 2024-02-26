from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path("api/v1/", include("apps.users.urls")),
    path("api/v1/", include("apps.reobjects.urls")),
    path("api/v1/", include("apps.village.urls")),
    path("api/v1/", include("apps.blog.urls")),
    path("api/v1/", include("apps.reviews.urls")),
    path("api/v1/", include("apps.applications.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path(r"mdeditor/", include("mdeditor.urls")),
]

urlpatterns += api_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
