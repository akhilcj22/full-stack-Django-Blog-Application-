# Django Blog Application

A fully-featured Django blog application with user authentication, CRUD operations, comments system, and responsive design.

## Features

### ✅ Core Features
- **User Authentication**: Registration, login, logout
- **Post Management**: Create, read, update, delete blog posts
- **Comments System**: Users can comment on posts
- **Categories**: Organize posts by categories
- **Admin Panel**: Full Django admin interface
- **Search Functionality**: Search posts by title, content, or author
- **Pagination**: Efficient pagination for posts and comments
- **Responsive Design**: Bootstrap-based responsive UI

### ✅ Advanced Features
- **Featured Posts**: Highlight important posts
- **View Count**: Track post popularity
- **User Profiles**: Author information and post history
- **Draft Posts**: Save posts as drafts
- **Post Statistics**: View counts, comment counts
- **Related Posts**: Show related posts by category
- **Sidebar Widgets**: Featured posts, categories, recent posts

### ✅ Security & Performance
- **User Permissions**: Only authors can edit/delete their posts
- **Form Validation**: Comprehensive form validation
- **SQL Injection Protection**: Django ORM protection
- **CSRF Protection**: Built-in CSRF protection
- **Optimized Queries**: Efficient database queries with select_related

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd django-blog
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv blog_env
   
   # On Windows
   blog_env\Scripts\activate
   
   # On macOS/Linux
   source blog_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create sample data (optional):**
   ```bash
   python manage.py populate_blog
   ```

6. **Start development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Blog: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
   - Login: admin / admin123 (if you ran populate_blog)

## Project Structure

```
django-blog/
├── blog/                          # Main blog application
│   ├── management/
│   │   └── commands/
│   │       └── populate_blog.py   # Sample data command
│   ├── migrations/                # Database migrations
│   ├── templates/blog/            # HTML templates
│   │   ├── base.html             # Base template
│   │   ├── home.html             # Home page
│   │   ├── post_detail.html      # Post detail page
│   │   ├── post_form.html        # Create/edit post form
│   │   ├── post_confirm_delete.html # Delete confirmation
│   │   ├── my_posts.html         # User's posts
│   │   ├── category_posts.html   # Posts by category
│   │   ├── login.html            # Login page
│   │   └── register.html         # Registration page
│   ├── admin.py                  # Admin configuration
│   ├── forms.py                  # Django forms
│   ├── models.py                 # Database models
│   ├── urls.py                   # URL patterns
│   └── views.py                  # View functions
├── blog_project/                 # Django project settings
│   ├── settings.py               # Development settings
│   ├── settings_production.py    # Production settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── staticfiles/                  # Collected static files
├── media/                        # User uploaded files
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── DEPLOYMENT.md                 # Deployment guide
```

## Models

### Post Model
- `title`: Post title
- `slug`: URL-friendly version of title
- `author`: User who created the post
- `content`: Post content
- `category`: Post category (optional)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `published`: Published status
- `featured`: Featured post flag
- `view_count`: Number of views

### Comment Model
- `post`: Related post
- `author`: Comment author
- `content`: Comment content
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `approved`: Approval status

### Category Model
- `name`: Category name
- `slug`: URL-friendly version of name
- `description`: Category description
- `created_at`: Creation timestamp

## API Endpoints

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | home | List all published posts |
| `/post/<slug>/` | post_detail | Display single post |
| `/category/<slug>/` | category_posts | Posts by category |
| `/post/create/` | post_create | Create new post |
| `/post/<slug>/edit/` | post_edit | Edit post |
| `/post/<slug>/delete/` | post_delete | Delete post |
| `/my-posts/` | my_posts | User's posts |
| `/register/` | register_view | User registration |
| `/login/` | login_view | User login |
| `/logout/` | logout_view | User logout |
| `/admin/` | admin | Django admin |

## Customization

### Adding New Features

1. **Create new models** in `models.py`
2. **Create migrations** with `python manage.py makemigrations`
3. **Apply migrations** with `python manage.py migrate`
4. **Create forms** in `forms.py`
5. **Add views** in `views.py`
6. **Create templates** in `templates/blog/`
7. **Update URLs** in `urls.py`

### Styling

The application uses Bootstrap 5 for styling. You can customize the appearance by:

1. **Modifying templates** in `templates/blog/`
2. **Adding custom CSS** in the base template
3. **Using Bootstrap classes** for consistent styling

### Database

The application uses SQLite by default. For production, consider using PostgreSQL:

1. **Install PostgreSQL** and psycopg2
2. **Update settings** to use PostgreSQL
3. **Run migrations** to create tables

## Testing

Run the Django test suite:

```bash
python manage.py test
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

Quick deployment options:
- **Railway**: Easiest for beginners
- **Render**: Good free tier
- **PythonAnywhere**: Python-focused hosting
- **Heroku**: Popular platform

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## Acknowledgments

- Django framework
- Bootstrap for UI components
- Font Awesome for icons
- The Django community for excellent documentation

---

**Happy Blogging! 🚀**
