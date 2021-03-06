from django.urls import path
from .views import *

urlpatterns = [
    path('field/', ListField.as_view()),
    path('field/<int:pk>/', DetailField.as_view()),
    path('field/activity/', ListActivity.as_view()),
    path('field/activity/<int:pk>', DetailActivity.as_view()),
    path('field/assign_activity/', ListSeason.as_view()),
    path('field/assign_activity/<int:pk>', DetailSeason.as_view()),
    # path('points/', points, name='points'),
]