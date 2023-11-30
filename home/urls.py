from django.urls import path
from .views import Homepage ,Aboutpage , Servecepage ,Contactpage ,register

urlpatterns = [
    path('' , Homepage , name='home'),
    path('about/' , Aboutpage , name='about'),
    path('servece/' , Servecepage , name='servece'),
    path('contact/' , Contactpage , name='contact'),
    path('register/' , register)
]
