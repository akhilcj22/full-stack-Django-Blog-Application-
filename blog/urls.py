from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    
    # CRUD operations - specific patterns first
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    
    # Post detail - general pattern last
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # Category patterns - specific first
    path('category/create/', views.category_create, name='category_create'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    
    # User-specific pages
    path('my-posts/', views.my_posts, name='my_posts'),
    
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
