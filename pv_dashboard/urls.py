# urls.py
from django.urls import path

#add more urls for more functions
from .views import TimeSeriesView
urlpatterns = [
    path('data/', TimeSeriesView.as_view()),
]

# This is only required to support extension-style formats (e.g. /data.csv)
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)