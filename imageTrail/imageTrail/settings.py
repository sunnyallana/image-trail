from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Handles the current session across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Associates users with requests using sessions. It also includes the following models: User, Group, and Permission
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imageTrail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'imageTrail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media files configuration. This is where the uploaded files will be stored
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


######################################################################  SEND EMAILS WITH DJANGO SETTINGS  ###############################################################################


# Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Uncomment the next line if you want to print email/s to the console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


######################################################################  LOGIN USING EMAIL SETTINGS  ###############################################################################

# Define a custom authentication backend to log in using email. Check the authentication.py file in the account app

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Default authentication backend
    'account.authentication.EmailAuthBackend', # Custom authentication backend to log in using email. Check the authentication.py file in the account app
]
    
######################################################################  SOCIAL AUTH SETTINGS  ###############################################################################

# Add accounts app to the start of the INSTALLED_APPS list. This is because the account app contains the custom authentication backend that we will use to log in using email

ALLOWED_HOSTS += [
    'mysite.com', 
    'localhost',
    '127.0.0.1',
]

# Install requirements: pip install -r requirements.txt

# Locate the hosts file of your machine. If you are using Linux or macOS, the hosts file is located at /etc/hosts.
# If you are using Windows, the hosts file is located at C:\Windows\System32\Drivers\etc\hosts.
# Edit the hosts file of your machine and add the following line to it [This line maps the IP address]: 127.0.0.1 mysite.com


INSTALLED_APPS += [
    'social_django', # Install using 'pip install social-auth-app-django'
    'django_extensions', # pip install git+https://github.com/django-extensions/django-extensions.
]

# Custom settings
LOGIN_REDIRECT_URL = 'dashboard' # Tells Django which URL to redirect the user to after a successful login if no next parameter is present in the request
LOGIN_URL = 'login' # The URL to redirect the user to log in (for example, views using the login_required decorator)
LOGOUT_URL = 'logout' # The URL to redirect the user to log out


# Social authentication settings
AUTHENTICATION_BACKENDS += [
    'social_core.backends.facebook.FacebookOAuth2', # To login with Facebook
    'social_core.backends.twitter.TwitterOAuth', # To login with Twitter
    'social_core.backends.google.GoogleOAuth2', # To login with Google OAUTH 2
]

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.getenv('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.getenv('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile', # We added this to the default pipeline
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]


############################################################################################################################################################################