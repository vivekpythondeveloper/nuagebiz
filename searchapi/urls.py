
from django.urls import path,include

from .views import Search


urlpatterns = [
    path('search', Search.as_view()),
]