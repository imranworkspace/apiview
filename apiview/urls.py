from django.contrib import admin
from django.urls import path
from api import views as v
# for static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',v.ViewClass.as_view()),
    path('get/<int:id>/',v.ViewClass.as_view()),
    path('get/<int:id>/update/',v.ViewClass.as_view()),
]
# Serving media files only during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# for production
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)