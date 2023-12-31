from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('author/', include('author.urls')),
    path('', views.home, name="homepage"),
    path('car', views.car, name="car"),
    path('categories/', include('categories.urls')),
    path('posts/', include('posts.urls')),
    path('bmw', views.bmw, name='BMW'),
    path('mercede', views.mercede, name='MERCEDE'),
    path('tata', views.tata, name='TATA'),
    path('all', views.all, name='ALL'),
     path('add_car/<int:id>/', views.add_car, name='add_car'),
    
   
]
  
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
