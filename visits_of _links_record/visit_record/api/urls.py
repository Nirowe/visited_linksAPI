from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('visited_links/', VisitedLinks),
    path('visited_domains/', GetStatisticTimeIntervar)
]
