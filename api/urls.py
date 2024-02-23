from django.urls import path
from api import views as v

urlpatterns = [
    path('get/',v.ViewClass.as_view(),name='get'),
    path('get/<int:id>/',v.ViewClass.as_view()),
    path('get/<int:id>/update/',v.ViewClass.as_view()),
]
