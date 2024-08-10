from django.urls import path
from .views import *
urlpatterns = [
    path('',HotelListAPIView.as_view(),name='hotels'),
    path('new/',HotelCreateView.as_view(),name='create'),
    path('detail/<int:pk>',HotelRUD.as_view(),name='update'),
]