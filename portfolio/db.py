from dotenv import load_dotenv
import os
load_dotenv()

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("NAME"),
    'USER': os.getenv("USER"),
    'PASSWORD': os.getenv("PASS"),
    'HOST': os.getenv("HOST"),
    'PORT': os.getenv("PORT"),
    'OPTIONS': {'sslmode': 'require'},
  }
}