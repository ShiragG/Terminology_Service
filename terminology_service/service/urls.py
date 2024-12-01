from django.urls import path, include

from service.views import RefBookListView, RefBookElementListView, RefBookCheckElementView

urlpatterns = [
    path('refbooks/', RefBookListView.as_view(), name='refbooks_list'),
    path('refbooks/<int:id>/elements', RefBookElementListView.as_view(), name='refbooks_elements'),
    path('refbooks/<int:id>/check_element', RefBookCheckElementView.as_view(), name='check_element'),
]