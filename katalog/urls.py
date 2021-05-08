from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produkty', views.produkty, name='produkty-list'),
    path('kategorie', views.kategorie, name='kategorie-list'),
    path('kolekce', views.kolekce, name='kolekce-list'),
    path('produkt/<int:pk>/', views.ProduktDetail.as_view(), name='produkt-detail'),
    path('kategorie/<int:pk>/', views.kategorieDetail, name='kategorie-detail'),
    path('kolekce/<int:pk>/', views.kolekceDetail, name='kolekce-detail')
]
