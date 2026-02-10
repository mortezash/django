from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blg/', views.blogs, name='blogs'),  # ← این آدرس دقیقاً میشه /blog/blg
    path('blg/<slug:slug>/', views.post_detail, name='post_detail'),  # URL داینامیک
]
