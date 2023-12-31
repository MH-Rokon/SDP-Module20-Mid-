

from django.urls import path
from . import views

urlpatterns = [
    
     
    path('buy_now/<int:car_id>/', views.buy_now, name='buy_now'),
    path('edit/<int:id>/', views.EditPostView.as_view(), name='edit_post'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
     path('buy/<int:id>/', views.buy, name='buy'),
   
    
  
 
]
