from django.urls import path
from .views import index
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import new_time
from .views import new_coordinate
from .views import ellipsoid



urlpatterns = [
    path('', index, name='index' ),
    path('time/', views.time, name='time' ),
    path('coordinate/', views.coordinate, name='coordinate' ),
    path('cartesian/', views.cartesian, name='cartesian' ),
    path('new_time/', new_time, name='new_time'),
    path('new_coordinate/', new_coordinate, name='new_coordinate'),
    path('ellipsoid/', ellipsoid, name='ellipsoid')
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)