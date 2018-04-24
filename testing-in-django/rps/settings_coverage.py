from .settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'django_nose',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=game',
]
