from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),

	path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('inbox/', views.inbox, name="inbox")
]