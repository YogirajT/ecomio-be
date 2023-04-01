from django.urls import path
from api.views import Destination, SearchData

urlpatterns = [
    path('destination', Destination.as_view()),
    path('search-data', SearchData.as_view())
]
