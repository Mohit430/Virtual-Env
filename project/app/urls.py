from django.urls import path
from . import views


urlpatterns=[
    path('render/',views.render1),
    path('redirect/',views.redirect1),
    path('HttpResponse/',views.HttpResponse1),
    path('JsonResponse/',views.JsonResponse1),
    path('data/',views.data,name='data'),
]