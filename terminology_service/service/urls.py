from django.urls import path, include
from rest_framework.routers import SimpleRouter

from service.views import RefBookViewSet, RefBookVersionViewSet, RefBookElementViewSet

router = SimpleRouter()

# router.register(r'refbooks', RefBookViewSet)
# router.register(r'refbooks-versions', RefBookVersionViewSet)
# router.register(r'refbooks-elements', RefBookElementViewSet)

# service_urlpatterns = [
#     path('', include(router.urls)),
# ]