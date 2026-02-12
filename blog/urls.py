from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('blg/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('edit/<slug:slug>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name='post_delete'),
]
