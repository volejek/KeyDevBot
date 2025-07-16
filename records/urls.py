from django.urls import path
from .views import ArrivalRecordViewSet


urlpatterns = [
    path('track/', ArrivalRecordViewSet.as_view(), name='arrival-record'),
]
