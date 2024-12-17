from django.urls import path, include
from assignment.views import index, projectDetail

urlpatterns = [
    path('', index, name="index"),
    path('project/<id>', projectDetail, name="ProjectDetail"),

]
