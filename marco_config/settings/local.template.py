# https://gist.github.com/ndarville/3452907
SECRET_KEY = 'FOOOOOOOO'

ALLOWED_HOSTS = ['marco.point97.io']

STATIC_ROOT = '/home/point97/webapps/marco_portal2_static'

# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql development headers)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'marco_portal',
        'USER': 'marco_portal',
        'PASSWORD': 'ALSO FOOOOOOO',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

