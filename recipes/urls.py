from django.urls import path
from .views import home
from .views import RecipesListView
from .views import RecipesDetailView
from .views import search
from .views import about

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipesListView.as_view(), name='list'),
    path('list/<pk>', RecipesDetailView.as_view(), name='detail'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
]
