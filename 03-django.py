try:
    import warnings
    from django.utils.deprecation import RemovedInDjango18Warning, RemovedInDjango19Warning
    warnings.filterwarnings(action="ignore", category=RemovedInDjango18Warning)
    warnings.filterwarnings(action="ignore", category=RemovedInDjango19Warning)
except ImportError:
    pass

def django_setup():
    import django
    django.setup()

def reset_django_connection():
    from django import db
    db.close_connection()
