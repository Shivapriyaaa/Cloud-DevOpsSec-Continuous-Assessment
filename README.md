# What'sToday - Social Blogging Platform

![Django](https://img.shields.io/badge/Django-5.0-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

What'sToday is a modern, dynamic cloud-based blogging platform built with Django. It provides a complete social media experience where users can create, share, and interact with blog posts through likes, comments, and following features.

## 🌟 Features

### Core Functionality
- **User Authentication**: Secure registration, login, and logout system
- **Blog Management**: Full CRUD operations for blog posts
  - Create new blog posts with rich content
  - Read and view all blog posts in a feed
  - Update your own blog posts
  - Delete your own blog posts
- **Profile Management**: Complete profile CRUD operations
  - Create and customize user profiles
  - Edit profile information (bio, location, website)
  - View other users' profiles
  - Delete user accounts

### Social Features
- **Like System**: Express appreciation for blog posts
- **Comment System**: Engage in discussions on blog posts
- **Follow System**: Follow other users to curate your feed
- **User Feed**: View all recent blog posts from the community

### User Experience
- **Modern UI**: Beautiful orange and white theme with Bootstrap 5
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Intuitive Navigation**: Easy-to-use interface for all features
- **Real-time Updates**: Dynamic content updates without page refresh

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.0
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Language**: Python 3.13
- **Architecture**: Model-View-Template (MVT) pattern

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.13 or higher
- pip (Python package installer)
- Git (for version control)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Code
```

### Step 2: Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

This allows you to access the Django admin panel at `/admin`.

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
Code/
├── blogsite/              # Django project settings
│   ├── __init__.py
│   ├── settings.py        # Application settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── core/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── models.py          # Data models (BlogPost, Comment, Like, Profile)
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   └── signals.py         # Signal handlers
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── core/              # App-specific templates
│       ├── home.html
│       ├── register.html
│       ├── login.html
│       ├── post_detail.html
│       ├── post_form.html
│       ├── profile.html
│       └── ...
├── static/                # Static files
│   └── css/
│       └── styles.css     # Custom styles
├── db.sqlite3             # SQLite database (created after migration)
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## 🎯 Usage Guide

### Getting Started

1. **Register an Account**
   - Navigate to the registration page
   - Fill in your username, email (optional), and password
   - Click "Register" to create your account

2. **Create Your First Blog Post**
   - After logging in, click "Write a blog" on the home page
   - Enter a title and content for your blog post
   - Click "Create" to publish

3. **Interact with Posts**
   - Like posts by clicking the "Like" button
   - Add comments by scrolling to the comment section
   - View post details by clicking on the post title

4. **Manage Your Profile**
   - Click on your username in the navigation bar
   - Edit your profile to add bio, location, and website
   - View your published posts on your profile page

5. **Follow Other Users**
   - Visit any user's profile page
   - Click "Follow" to follow them
   - Their posts will appear in your feed

### Key URLs

- Home: `/`
- Register: `/register/`
- Login: `/login/`
- Create Post: `/post/create/`
- Profile: `/profile/<username>/`
- Admin Panel: `/admin/` (requires superuser)

## 🔒 Security Features

- **CSRF Protection**: All forms are protected against Cross-Site Request Forgery attacks
- **Password Hashing**: Passwords are securely hashed using Django's PBKDF2 algorithm
- **Input Validation**: All user inputs are validated through Django forms
- **SQL Injection Protection**: Django ORM automatically escapes all database queries
- **Authentication Required**: Sensitive operations require user authentication
- **Secure Sessions**: Session management with secure cookie settings

## 🧪 Testing

To run the test suite (if tests are added):

```bash
python manage.py test
```

## 🚢 Deployment

### Production Considerations

1. **Environment Variables**: Set `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` in production
2. **Database**: Migrate from SQLite to PostgreSQL for production
3. **Static Files**: Run `python manage.py collectstatic` and configure static file serving
4. **HTTPS**: Configure SSL/TLS certificates for secure connections
5. **Cloud Platform**: Deploy to AWS, Azure, or GCP using appropriate services

### Example Environment Variables

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 🤝 Contributing

This is an academic project. For contributions or suggestions, please contact the project maintainer.

## 📝 License

Copyright © 2025 What'sToday. All rights reserved.

## 👨‍💻 Author

[Your Name]
[Student Number]
National College of Ireland

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [Python Documentation](https://docs.python.org/3/)

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`
- **Solution**: Ensure your virtual environment is activated and run `pip install -r requirements.txt`

**Issue**: `no such table: core_blogpost`
- **Solution**: Run `python manage.py makemigrations` followed by `python manage.py migrate`

**Issue**: Static files not loading
- **Solution**: Ensure `DEBUG=True` in development or configure static file serving for production

**Issue**: Port already in use
- **Solution**: Use a different port: `python manage.py runserver 8001`

## 📊 Database Models

### BlogPost
- `title`: CharField (max 150 characters)
- `content`: TextField
- `author`: ForeignKey to User
- `created_at`: DateTimeField
- `updated_at`: DateTimeField

### Comment
- `post`: ForeignKey to BlogPost
- `author`: ForeignKey to User
- `content`: TextField
- `created_at`: DateTimeField

### Like
- `user`: ForeignKey to User
- `post`: ForeignKey to BlogPost
- `created_at`: DateTimeField

### Profile
- `user`: OneToOneField to User
- `bio`: TextField
- `location`: CharField
- `website`: URLField
- `following`: ManyToManyField to self

## 🎨 Customization

### Changing the Theme Colors

Edit `static/css/styles.css` to customize the orange and white color scheme:

```css
:root {
    --orange-primary: #ff6b35;  /* Change this */
    --white-bg: #ffffff;         /* Change this */
}
```

### Adding New Features

1. Create models in `core/models.py`
2. Create forms in `core/forms.py`
3. Add views in `core/views.py`
4. Create templates in `templates/core/`
5. Update URLs in `core/urls.py`
6. Run migrations: `python manage.py makemigrations && python manage.py migrate`

---

**Built with ❤️ using Django and Bootstrap**

