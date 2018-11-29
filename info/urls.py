from django.urls import path
from . import views

# app_name defines a namespace used in reverse url mapping, e.g. 'polls:index'
app_name = "info"
urlpatterns = [
    path("",views.show_request, name="index"),
]
