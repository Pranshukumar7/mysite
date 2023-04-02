from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdsListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdsDetailView.as_view(), name='ads_detail'),
    path('ad/create',
        views.AdsCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_create'),
    path('ad/<int:pk>/update',
        views.AdsUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_update'),
    path('ad/<int:pk>/delete',
        views.AdsDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ads_delete'),
]