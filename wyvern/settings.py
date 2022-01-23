"""
Django settings for wyvern project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import socket
import configparser

from qr_code.qrcode import constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Detect Site From Settings
# https://stackoverflow.com/questions/54933044/different-settings-py-file-for-different-domains-in-django


# Wyvern: Parsing Config
"""
    Modify config file to reflect vendor/pod changes
"""
config = configparser.RawConfigParser()
config.read("./config.cnf")

database = config.get("database", "database")
username = config.get("database", "username")
password = config.get("database", "password")
hostname = config.get("database", "hostname")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get("application", "debug") == "True"

ALLOWED_HOSTS = config.get("hosts", "allowed").split("\n")

# Application definition

INSTALLED_APPS = [
    "wyvernuser",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # QR Code,
    "qr_code",
    # Optimization
    "compressor",
    # User Agents - Detect Mobile
    "django_user_agents",
    # Wyvern API
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    # Miscellaneous Modules
    "ckeditor",
    "ckeditor_uploader",
    "djmoney",
    "crispy_forms",
    "django_countries",
    # Wyvern Apps
    "wyvern",
    "wyvernthemes",
    "wyvernsite",
    "wyverntrace",
    # Bootstrap 4
    "django-bs4",
    "django.forms",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Other Middleware
    # User Agents
    "django_user_agents.middleware.UserAgentMiddleware",
]

ROOT_URLCONF = "wyvern.urls"

#####################
# Template Settings #
#####################

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                #############################
                # Wyvern Context Processors #
                #############################
                "wyvern.context.spam_filters",
                "wyvernsite.context.sites",
                "wyvernthemes.context.themes",
                "wyvernthemes.context.theme_config",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates").replace("\\", "/"),
    os.path.join(PROJECT_ROOT, "/").replace("\\", "/"),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    #     'django.template.loaders.eggs.Loader',
)

#########################
# End Template Settings #
#########################

#############################
# Static and Media Settings #
#############################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # other finders..
    "compressor.finders.CompressorFinder",
)

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#################################
# End Static and Media Settings #
#################################

WSGI_APPLICATION = "wyvern.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": database,
        "USER": username,
        "PASSWORD": password,
        "HOST": hostname,
        "PORT": "",
    }
}

############################
# Authentication and Login #
############################

# Password Validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "wyvernuser.User"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_L10N = True

USE_TZ = True

##################
# Boostrap Forms #
##################

CRISPY_TEMPLATE_PACK = "bootstrap4"

###################
# Message Storage #
###################

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

############
# CKEditor #
############
CKEDITOR_BASEPATH = STATIC_URL + "/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_FILENAME_GENERATOR = "wyvern.util.upload.get_ck_file_path"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Advanced",
        "height": "300px",
        "width": "100%",
    },
}
# CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
# CKEDITOR_BROWSE_SHOW_DIRS = True
# CKEDITOR_RESTRICT_BY_DATE = True
# CKEDITOR_STORAGE_BACKEND = MEDIA_ROOT + "/uploads/ckeditor/"
# CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (100, 100)
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 95

################
# Google Email #
################

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""


################
# GoDaddy Email #
################

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtpout.asia.secureserver.net'
# EMAIL_HOST_USER = ''
# DEFAULT_FROM_EMAIL = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = "default"
