from dotenv import load_dotenv
import os
load_dotenv()

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': os.getenv("USER"),
    'PASSWORD': os.getenv("PASS"),
    'HOST': 'ep-plain-limit-71331214.ap-southeast-1.aws.neon.tech',
    'PORT': '5432',
    'OPTIONS': {'sslmode': 'require'},
  }
}