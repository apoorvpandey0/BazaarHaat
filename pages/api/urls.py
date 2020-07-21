from django.urls import path

from . import views

urlpatterns = [
    path('slide/list/',views.SlideListAPIView.as_view(),name = 'api-Slide-list'),
]
