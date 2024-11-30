from django.urls import path, include

from service.views import RefBookListView, RefBookElementListView

service_urlpatterns = [
    path('refbooks/', RefBookListView.as_view()),
    path('refbooks/<int:id>/elements', RefBookElementListView.as_view()),
]