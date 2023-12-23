from django.urls import path
from .views import index
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index' ),
    path('time/', views.time, name='time' ),
    path('coordinate/', views.coordinate, name='coordinate' ),
    path('cartesian/', views.cartesian, name='cartesian' ),
    
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)