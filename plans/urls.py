from django.urls import path
from . import views

urlpatterns = [
    # legt das Home-Template für die URL ohne Zusätzen fest
    path('', views.home, name="plans-home")
]