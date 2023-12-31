from django.urls import path
from  author import views

urlpatterns = [
    
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="login"),
    path('profile/', views.profile,name="profile"),
    path('changepass/', views.change_password,name="changepass"),
    path('updateprofile/', views.updateprofile,name="updateprofile"),
    path('logout/', views.user_logout,name="logout"),

 
   
]
