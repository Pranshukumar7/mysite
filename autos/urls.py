from django.urls import path
from . import views
app_name = 'autos'
urlpatterns = [
path("",views.MainView.as_view(),name = "index"),
path('main/create',views.AutosCreateView.as_view(),name = "autos_create"),
path('main/<int:pk>/update',views.AutosUpdateView.as_view(),name = "autos_update"),
path('main<int:pk>/delete',views.AutosDeleteView.as_view(),name = "autos_delete"),
path('lookup/',views.MakeView.as_view(),name = "make_list"),
path('lookup/create/',views.MakeCreate.as_view(),name = "make_create"),
path('lookup/<int:pk>/update',views.MakeUpdate.as_view(),name = "make_update"),
path('lookup/<int:pk>/delete',views.MakeDelete.as_view(),name = "make_delete")
]

