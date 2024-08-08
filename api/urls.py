from django.urls import path
from .views import *
urlpatterns = [
    path('',HotelListAPIView.as_view(),name='HotelApi'),
    path('new/',HotelCreateView.as_view(),name='CRUD'),
    path('hotel/<int:pk>',HotelRUD.as_view(),name='Detail'),
]