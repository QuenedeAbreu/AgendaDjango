from django.urls import path
from .views import index_view_app

urlpatterns = [
    path('', index_view_app),
]
