from django.urls import path, include
from assignment.views import index

urlpatterns = [
    path('', index, name="index"),

]
