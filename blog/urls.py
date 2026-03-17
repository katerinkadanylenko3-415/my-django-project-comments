from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
    path('category/<slug:slug>', views.category, name="category"),
    path('tag/<slug:slug>/', views.tag_posts, name="tag_posts"),
]
