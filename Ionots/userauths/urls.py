from django.urls import path, include
from userauths.views import RegisterView, Loginview, LogOutView

urlpatterns = [
    path('register/', RegisterView, name="RegisterView"),
    path('login/', Loginview, name="Loginview"),
    path('logout/', LogOutView, name="LogOutView"),

]
