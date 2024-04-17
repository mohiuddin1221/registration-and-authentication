
from django.urls import path
from .import views 


urlpatterns = [
     path('register/', views.Register.as_view(), name='register'),
     path('my_login/', views.MyLogin.as_view(), name = 'my_login'),
     path('dashboard/', views.dashbord, name = 'dashboard'),
     

]