# Django Blog App

A full-featured blog application built with Django, featuring user authentication, post management, and custom profile system.

## Features

- **User Authentication**: Register, login, logout functionality
- **User Profiles**: Custom user profiles with profile pictures
- **Blog Posts**: Create, read, update, and delete blog posts
- **Post Pagination**: Easy navigation through multiple posts
- **Responsive Design**: Bootstrap 5 for mobile-friendly interface
- **Password Toggle**: Show/hide password functionality on all password fields
- **Profile Management**: Update user information and profile pictures

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite3 (development)
- **Image Processing**: Pillow

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/MikeJohnsonisthename/Django-Blog-App.git
   cd Django-Blog-App
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Creating an Account
1. Navigate to the Register page
2. Fill in your username, email, and password
3. Click "Sign Up"

### Creating a Blog Post
1. Log in to your account
2. Click "New Post" in the navigation bar
3. Enter your post title and content
4. Click "Post"

### Managing Your Profile
1. Click "Profile" in the navigation bar
2. Update your profile picture and user information
3. Click "Update"

## Project Structure

```
Django-Blog-App/
├── blog/                 # Main blog application
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, images
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   └── urls.py          # URL routing
├── users/               # User authentication app
│   ├── models.py        # User profile model
│   ├── forms.py         # User forms
│   └── views.py         # User views
├── media/               # User uploaded files
├── mike_project/        # Project settings
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Mike Johnson - [@MikeJohnsonisthename](https://github.com/MikeJohnsonisthename)

Project Link: [https://github.com/MikeJohnsonisthename/Django-Blog-App](https://github.com/MikeJohnsonisthename/Django-Blog-App)

## Acknowledgments

- Bootstrap for the responsive design framework
- Django documentation and community
- Font Awesome for icons