from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post, Comment


class Command(BaseCommand):
    help = 'Populate the blog with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': 'Technology', 'description': 'Latest tech news and tutorials'},
            {'name': 'Programming', 'description': 'Programming tutorials and tips'},
            {'name': 'Web Development', 'description': 'Web development guides and resources'},
            {'name': 'Django', 'description': 'Django framework tutorials and tips'},
            {'name': 'Python', 'description': 'Python programming articles'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create a sample user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write('Created admin user (username: admin, password: admin123)')

        # Create sample posts
        posts_data = [
            {
                'title': 'Getting Started with Django',
                'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

In this tutorial, we'll cover the basics of Django, including:
- Setting up your development environment
- Creating your first Django project
- Understanding the MVT (Model-View-Template) pattern
- Working with models and databases
- Creating views and templates

Django comes with many built-in features that make web development easier, including:
- An admin interface
- User authentication
- Database migrations
- Security features
- And much more!

Let's get started with creating your first Django application.''',
                'category': 'Django',
                'featured': True,
            },
            {
                'title': 'Python Best Practices for Beginners',
                'content': '''Python is an excellent programming language for beginners due to its simple syntax and readability. However, writing Python code that follows best practices will make your code more maintainable, efficient, and professional.

Here are some essential Python best practices:

1. **Follow PEP 8 Style Guide**
   - Use 4 spaces for indentation
   - Limit lines to 79 characters
   - Use meaningful variable names

2. **Use Virtual Environments**
   - Always use virtual environments for your projects
   - This prevents package conflicts between projects

3. **Write Docstrings**
   - Document your functions and classes
   - Use triple quotes for docstrings

4. **Handle Exceptions Properly**
   - Use try-except blocks for error handling
   - Don't use bare except clauses

5. **Use List Comprehensions**
   - They're more Pythonic and often faster
   - Great for simple transformations

Remember, good code is not just working code, but code that others can easily understand and maintain!''',
                'category': 'Python',
                'featured': True,
            },
            {
                'title': 'Building Responsive Websites with Bootstrap',
                'content': '''Bootstrap is a powerful front-end framework that makes it easy to create responsive, mobile-first websites. It provides a comprehensive set of CSS classes and JavaScript components that can be used to build modern web applications.

Key features of Bootstrap include:
- Responsive grid system
- Pre-built components (buttons, forms, navigation, etc.)
- Utility classes for spacing, colors, and typography
- JavaScript plugins for interactive elements

Getting started with Bootstrap is simple:
1. Include Bootstrap CSS and JS files
2. Use the grid system for layout
3. Apply component classes to elements
4. Customize with your own CSS

The grid system is based on a 12-column layout, making it easy to create responsive designs that work on all device sizes. You can use classes like col-sm-6, col-md-4, and col-lg-3 to control how columns behave on different screen sizes.

Bootstrap also includes many useful components like:
- Navigation bars
- Cards
- Modals
- Carousels
- Forms
- And much more!

Whether you're building a simple website or a complex web application, Bootstrap can help you create a professional-looking, responsive design quickly and efficiently.''',
                'category': 'Web Development',
                'featured': False,
            },
            {
                'title': 'Understanding Django Models and Databases',
                'content': '''Django models are the heart of any Django application. They define the structure of your data and provide an abstraction layer for database operations. Understanding how to work with models effectively is crucial for Django development.

Key concepts in Django models:

1. **Model Definition**
   - Models are Python classes that inherit from django.db.models.Model
   - Each attribute represents a database field
   - Django automatically creates database tables from models

2. **Field Types**
   - CharField for short text
   - TextField for long text
   - IntegerField for numbers
   - DateTimeField for dates and times
   - ForeignKey for relationships

3. **Database Migrations**
   - Migrations track changes to your models
   - Use makemigrations to create migration files
   - Use migrate to apply migrations to the database

4. **QuerySets**
   - QuerySets allow you to retrieve data from the database
   - They're lazy and chainable
   - Use methods like filter(), exclude(), and get()

5. **Model Relationships**
   - One-to-Many: ForeignKey
   - Many-to-Many: ManyToManyField
   - One-to-One: OneToOneField

Working with models effectively will make your Django applications more robust and maintainable.''',
                'category': 'Django',
                'featured': False,
            },
            {
                'title': 'The Future of Web Development',
                'content': '''Web development is constantly evolving, with new technologies and frameworks emerging regularly. As we look to the future, several trends are shaping the landscape of web development.

Emerging trends in web development:

1. **Progressive Web Apps (PWAs)**
   - Combine the best of web and mobile apps
   - Work offline and can be installed on devices
   - Provide native app-like experiences

2. **Serverless Architecture**
   - Functions as a Service (FaaS)
   - Reduced server management overhead
   - Automatic scaling and cost optimization

3. **JAMstack**
   - JavaScript, APIs, and Markup
   - Static site generation with dynamic functionality
   - Better performance and security

4. **WebAssembly (WASM)**
   - Near-native performance in browsers
   - Enables running code written in other languages
   - Great for performance-critical applications

5. **AI and Machine Learning Integration**
   - AI-powered features in web applications
   - Automated testing and optimization
   - Enhanced user experiences

6. **Voice User Interfaces**
   - Voice-controlled web applications
   - Integration with smart speakers
   - Accessibility improvements

As developers, staying current with these trends and learning new technologies will be essential for building modern, competitive web applications.''',
                'category': 'Technology',
                'featured': True,
            },
        ]

        for post_data in posts_data:
            category = categories[post_data['category']]
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'content': post_data['content'],
                    'author': user,
                    'category': category,
                    'featured': post_data['featured'],
                    'published': True,
                }
            )
            if created:
                self.stdout.write(f'Created post: {post.title}')

        # Create some sample comments
        comments_data = [
            {
                'post_title': 'Getting Started with Django',
                'content': 'Great tutorial! This really helped me understand the basics of Django.',
                'author': user,
            },
            {
                'post_title': 'Getting Started with Django',
                'content': 'Thanks for sharing this. The MVT pattern explanation was very clear.',
                'author': user,
            },
            {
                'post_title': 'Python Best Practices for Beginners',
                'content': 'Excellent article! I wish I had read this when I was starting with Python.',
                'author': user,
            },
        ]

        for comment_data in comments_data:
            try:
                post = Post.objects.get(title=comment_data['post_title'])
                comment, created = Comment.objects.get_or_create(
                    post=post,
                    author=comment_data['author'],
                    content=comment_data['content'],
                )
                if created:
                    self.stdout.write(f'Created comment for: {post.title}')
            except Post.DoesNotExist:
                self.stdout.write(f'Post not found: {comment_data["post_title"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the blog with sample data!')
        )
