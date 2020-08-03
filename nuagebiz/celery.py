import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nuagebiz.settings')

celery_app = Celery('nuagebiz')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()