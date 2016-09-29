def django_setup():
    import django
    django.setup()

def reset_django_connection():
    from django import db
    db.close_connection()
