from django.urls import path
from .views import AdsListView, AdsCreateView, AdsDetailView, AdsSearchView

app_name = 'ads'
urlpatterns = [
    path('advertisments', AdsListView.as_view(), name='home'),
    path('create', AdsCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AdsDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', AdsUpdateView.as_view(), name='update'),
    path('search', AdsSearchView.as_view(), name='search')
]