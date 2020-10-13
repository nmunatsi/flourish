"""
Django settings for flourish project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r2+kl0ci5#p_h4(e4edde8zko5ch%pp^jc-3z%rvh@fzmtv%09'

SITE_ID = 40

REVIEWER_SITE_ID = 1

APP_NAME = 'flourish'

AUTO_CREATE_KEYS = False

LOGIN_REDIRECT_URL = 'home_url'

ETC_DIR = '/etc'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django_q',
    'django_extensions',
    'crispy_forms',
    'edc_action_item.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'flourish_dashboard.apps.AppConfig',
    'flourish_maternal.apps.AppConfig',
    'flourish_child.apps.AppConfig',
    'flourish_follow.apps.AppConfig',
    'flourish.apps.EdcAppointmentAppConfig',
    'flourish.apps.EdcBaseAppConfig',
    'flourish.apps.EdcDataManagerAppConfig',
    'flourish.apps.EdcProtocolAppConfig',
    'flourish.apps.EdcVisitTrackingAppConfig',
    'flourish.apps.EdcTimepointAppConfig',
    'flourish.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'flourish.urls'

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

WSGI_APPLICATION = 'flourish.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(ETC_DIR, APP_NAME, 'mysql.conf'),
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'flourish_dashboard:subject_listboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'maternal_screening_listboard_url': 'flourish_dashboard:maternal_screening_listboard_url',
    'maternal_dataset_listboard_url': 'flourish_dashboard:maternal_dataset_listboard_url',
    'flourish_follow_listboard_url': 'flourish_follow:flourish_follow_listboard_url',

}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'flourish/base.html',
    'dashboard_base_template': 'flourish/base.html',
    'subject_listboard_template': 'flourish_dashboard/maternal_subject/listboard.html',
    'maternal_screening_listboard_template': 'flourish_dashboard/screening/maternal_listboard.html',
    'maternal_dataset_listboard_template': 'flourish_dashboard/maternal_dataset/maternal_listboard.html',
    'flourish_follow_listboard_template': 'flourish_follow/follow_listboard.html',
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'flourish', 'static')
