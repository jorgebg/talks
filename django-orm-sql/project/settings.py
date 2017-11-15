INSTALLED_APPS = [
    'blog',
    'django_extensions',
]

DEBUG = True
SHELL_PLUS_PRINT_SQL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

SECRET_KEY = 'I like trains'
