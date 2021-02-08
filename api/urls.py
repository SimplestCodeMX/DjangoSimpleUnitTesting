
from django.contrib import admin
from django.urls import path, include
from . import views as api_view
app_name = 'api'
urlpatterns = [
    path('', api_view.ListUsers.as_view(), name="list"),
    path('<int:id>/', api_view.DetailUser.as_view(), name="detail"),
]
