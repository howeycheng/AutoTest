"""
Django settings for AutoTest project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=^1@ml&ebo45ky2pwiaj#^&uj_twu5)c-uc1gh6^x@v6p=f2(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.apps.CasesConfig',
    'manager.apps.ManagerConfig',
    'mptt',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'manager.disable_csrf_check.DisableCSRFCheck',
    'backend.project_selector.ProjectSelector'
]

ROOT_URLCONF = 'AutoTest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')]
        ,
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

WSGI_APPLICATION = 'AutoTest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
PROJECT_NAME = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manager',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
DATABASE_ROUTERS = ['dynamic_db_router.DynamicDbRouter']
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 前端路径
FRONTEND_ROOT = 'frontend/dist'

# 静态资源地址
STATIC_URL = '/static/'
# Add for vue.js

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, FRONTEND_ROOT),
    os.path.join(BASE_DIR, FRONTEND_ROOT + '/static/'),
)

# 跨域设置
# 允许携带cookie
CORS_ALLOW_CREDENTIALS = True
# 只允许指定域访问
CORS_ORIGIN_ALLOW_ALL = False
# 针对跨域的http请求进行配置，localhost无法进行session传递
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
)
SESSION_COOKIE_PATH = "/"  # 作用路径，/代表所有路径下均起作用
# 由于开发阶段，前台访问后台API存在跨域问题，而新版google对cookies新增的samesite属性会导致无法跨域传递cookies,所以开发调试阶段，通过禁用浏览器上的samesite方式暂时解决该问题，待上线后，可使用nginx映射解决该问题
# 浏览器禁用方法
# chrome://flags/#site-isolation-trial-opt-out，搜索samesite
# 重启浏览器
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = 'None'

# 针对CSR配置
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = False

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

# 跨域允许的请求头
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
# rocketmq设置
ROCKET_MQ = {
    'nameSrv': '10.1.160.162:9876',
    'logConsumerName': 'logReceive',
    'casesProducerName': 'casesSend',
}
