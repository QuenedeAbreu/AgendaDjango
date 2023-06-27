from django.urls import path
from agenda.api.viewset import index_view_app

urlpatterns = [
    path('', index_view_app),
]
