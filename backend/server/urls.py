from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from api.routers import router

urlpatterns = [
	path('api/', include(router.urls)),
	path('api/', include(('api.urls', 'api'), namespace='api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TODO: turn back on
