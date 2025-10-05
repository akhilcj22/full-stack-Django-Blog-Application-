from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.db import models
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm, CategoryForm
from django.core.paginator import Paginator


def home(request):
    """Home page displaying all published posts"""
    posts = Post.objects.filter(published=True).select_related('author', 'category')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(
            models.Q(title__icontains=search_query) | 
            models.Q(content__icontains=search_query) |
            models.Q(author__username__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get featured posts for sidebar
    featured_posts = Post.objects.filter(published=True, featured=True)[:3]
    
    # Get categories for sidebar
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'featured_posts': featured_posts,
        'categories': categories,
        'search_query': search_query,
    }
    
    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    """Display a single post with its comments"""
    post = get_object_or_404(Post, slug=slug, published=True)
    
    # Handle comment submission
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    
    # Increment view count
    post.view_count += 1
    post.save(update_fields=['view_count'])
    
    # Get approved comments for this post
    comments = post.comments.filter(approved=True).select_related('author')
    
    # Get related posts (same category, excluding current post)
    related_posts = Post.objects.filter(
        category=post.category,
        published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
        'form': form,
    }
    
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, slug):
    """Display posts by category"""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(
        category=category,
        published=True
    ).select_related('author')
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    
    return render(request, 'blog/category_posts.html', context)


@login_required
def post_create(request):
    """Create a new post"""
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(user=request.user)
    
    return render(request, 'blog/post_form.html', {
        'form': form,
        'title': 'Create New Post',
        'submit_text': 'Create Post'
    })


@login_required
def post_edit(request, slug):
    """Edit an existing post"""
    post = get_object_or_404(Post, slug=slug)
    
    # Check if user is the author
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('blog:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post, user=request.user)
    
    return render(request, 'blog/post_form.html', {
        'form': form,
        'post': post,
        'title': 'Edit Post',
        'submit_text': 'Update Post'
    })


@login_required
def post_delete(request, slug):
    """Delete a post"""
    post = get_object_or_404(Post, slug=slug)
    
    # Check if user is the author
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('blog:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('blog:home')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def add_comment(request, slug):
    """Add a comment to a post"""
    post = get_object_or_404(Post, slug=slug, published=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form
    })


@login_required
def my_posts(request):
    """Display user's own posts"""
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/my_posts.html', {
        'page_obj': page_obj,
        'title': 'My Posts'
    })


@login_required
def category_create(request):
    """Create a new category (admin only)"""
    if not request.user.is_staff:
        messages.error(request, 'Only staff members can create categories.')
        return redirect('blog:home')
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('blog:home')
    else:
        form = CategoryForm()
    
    return render(request, 'blog/category_form.html', {
        'form': form,
        'title': 'Create New Category',
        'submit_text': 'Create Category'
    })


def register_view(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('blog:home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('blog:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('blog:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            next_url = request.GET.get('next', 'blog:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'blog/login.html')


def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('blog:home')
