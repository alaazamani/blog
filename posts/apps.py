from django.apps import AppConfig

from .models import Post

admin.site,register(Post)