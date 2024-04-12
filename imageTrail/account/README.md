# Django User Authentication with Email Integration

This Django application provides user authentication with email integration, allowing users to log in using their username or email address. It also includes a feature for password recovery, where users can request a password reset email.

## Getting Started

Follow these steps to integrate this application into your Django project:

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone or download the repository containing the Django application code.

2. Copy the `account` directory into your Django project directory.

3. Add `account` to your `INSTALLED_APPS` in `settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'account',
        ...
    ]
    ```

4. Update your `settings.py` to include the necessary configurations (as mentioned in the previous section).

    ```python
    # Django User Authentication Settings

    LOGIN_REDIRECT_URL = 'dashboard'
    LOGIN_URL = 'login'
    LOGOUT_URL = 'logout'

    # Email server configuration
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_HOST_USER = 'your_email@example.com'
    EMAIL_HOST_PASSWORD = 'your_email_password'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    # Media files configuration
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    # Custom authentication backend to allow login using email
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend', # Default authentication backend
        'account.authentication.EmailAuthBackend', # Custom authentication backend to log in using email
    ]
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. To use the user authentication features, include the necessary URLs in your project's `urls.py`:

    ```python
    from django.urls import path, include
    
    urlpatterns = [
        ...
        path('accounts/', include('account.urls')),
        ...
    ]
    ```

2. Start the development server:

    ```bash
    python manage.py runserver
    ```

3. Access the application in your browser and navigate to the login page (`/accounts/login`) to start using the authentication features.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need for user authentication with email integration in Django applications.