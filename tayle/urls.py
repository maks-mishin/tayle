from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path("signup/", include("users.urls")),
    path("", include("wallet.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
