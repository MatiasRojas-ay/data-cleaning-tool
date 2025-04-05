from django.urls import path
from .views import CleanFileView

urlpatterns = [
    path("clean/", CleanFileView.as_view(), name="clean-file"),
]