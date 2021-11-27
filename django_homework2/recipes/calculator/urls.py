from django.urls import path, include
from calculator.views import dish_view

urlpatterns = [
    path('<dish>/', dish_view),
]
