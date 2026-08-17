"""
Django settings for mysite project.

Glitter Scoops
"""

from pathlib import Path


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = "django-insecure-change-this-key"

# Local development
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Django built-in applications

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    # Glitter Scoops application

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
# ROOT URL
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
# The Glitter Scoops order and staff information is currently
# stored in JSON files.
#
# SQLite is still configured because Django uses its database
# for sessions and other Django functionality.
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
# LANGUAGE / TIME ZONE
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"


# Directory created by:
#
# python manage.py collectstatic
#

STATIC_ROOT = BASE_DIR / "staticfiles"


# Additional static files directory

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
# SESSION CONFIGURATION
# ============================================================

# Django database-backed sessions

SESSION_ENGINE = (
    "django.contrib.sessions.backends.db"
)


# Cookie name

SESSION_COOKIE_NAME = (
    "glitterscoops_session"
)


# Session lifetime = 8 hours

SESSION_COOKIE_AGE = (
    60 * 60 * 8
)


# Session expires when browser closes

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Save session for every request

SESSION_SAVE_EVERY_REQUEST = True


# ============================================================
# LOGIN / LOGOUT
# ============================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/orders/"

LOGOUT_REDIRECT_URL = "/login/"


# ============================================================
# GLITTER SCOOPS JSON DATABASE
# ============================================================

# ------------------------------------------------------------
# Staff Users
# ------------------------------------------------------------
#
# Expected location:
#
# home/database/staff_users.json
#

STAFF_USERS_FILE = (
    BASE_DIR
    / "home"
    / "database"
    / "staff_users.json"
)


# ------------------------------------------------------------
# Orders
# ------------------------------------------------------------
#
# Expected location:
#
# home/database/orders.json
#

ORDERS_FILE = (
    BASE_DIR
    / "home"
    / "database"
    / "orders.json"
)


# ============================================================
# SECURITY SETTINGS
# ============================================================
#
# These settings are suitable for local development.
#
# HTTPS-related settings should be enabled only after
# configuring HTTPS on your production server.
# ============================================================

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"


# ============================================================
# CSRF
# ============================================================

CSRF_COOKIE_HTTPONLY = False


# ============================================================
# PRODUCTION SECURITY
# ============================================================
#
# DO NOT enable these while using:
#
# http://127.0.0.1:8000/
#
# After GoDaddy HTTPS is configured, you can enable them.
#
# SECURE_SSL_REDIRECT = True
#
# SESSION_COOKIE_SECURE = True
#
# CSRF_COOKIE_SECURE = True
#
# SECURE_HSTS_SECONDS = 31536000
#
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#
# SECURE_HSTS_PRELOAD = True
#
# ============================================================