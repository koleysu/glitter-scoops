"""
Django settings for mysite project.

Glitter Scoops
"""

from pathlib import Path
import os


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = "django-insecure-change-this-in-production"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "glitterscoops.com",
    "www.glitterscoops.com",
    "glitter-scoops-1.onrender.com"
]


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Django Applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Glitter Scoops Application
    "home",
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = "mysite.urls"


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "home" / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = "mysite.wsgi.application"


# ============================================================
# DATABASE
# ============================================================
#
# Your current Glitter Scoops project uses JSON files
# for Orders and Staff Users.
#
# Django's built-in database is still configured because
# Django requires it for sessions and authentication.
#
# SQLite is perfectly fine for your current local project.
#

DATABASES = {

    "default": {

        "ENGINE":
            "django.db.backends.sqlite3",

        "NAME":
            BASE_DIR / "db.sqlite3",

    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"


# Location where Django will collect static files
# when using:
#
# python manage.py collectstatic
#

STATIC_ROOT = BASE_DIR / "staticfiles"


# Additional static directories
#

STATICFILES_DIRS = [

    BASE_DIR / "home" / "static",

]


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================================================
# SESSION SETTINGS
# ============================================================

# Session is required for your protected /orders/ page.

SESSION_ENGINE = (
    "django.contrib.sessions.backends.db"
)

SESSION_COOKIE_NAME = "glitterscoops_session"

SESSION_COOKIE_AGE = 60 * 60 * 8

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SAVE_EVERY_REQUEST = True


# ============================================================
# LOGIN SETTINGS
# ============================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/orders/"

LOGOUT_REDIRECT_URL = "/login/"


# ============================================================
# JSON DATABASE PATHS
# ============================================================

# Orders JSON file

ORDERS_FILE = (
    BASE_DIR
    / "home"
    / "database"
    / "orders.json"
)


# Staff Users JSON file

STAFF_USERS_FILE = (
    BASE_DIR
    / "home"
    / "database"
    / "staff_users.json"
)


# ============================================================
# SECURITY SETTINGS - LOCAL DEVELOPMENT
# ============================================================

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"


# ============================================================
# CSRF
# ============================================================

CSRF_COOKIE_HTTPONLY = False


# ============================================================
# PRODUCTION SETTINGS
# ============================================================
#
# DO NOT ENABLE THESE while running:
#
# http://127.0.0.1:8000/
#
# Enable them after HTTPS is configured on GoDaddy.
#
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
#
# ============================================================
