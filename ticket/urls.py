from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('register/',views.Register.as_view(),name='register'),
    path('result-table-mostafa/',views.Result.as_view(),name='result'),
]