from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
  path('pokemon/create', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
  path('pokemon/<int:pokemon_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('pokemon/<int:pokemon_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]