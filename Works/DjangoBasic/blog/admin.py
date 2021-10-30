from django.contrib import admin

# Register your models here.

from .models import Blog


class BlogAdmin(admin.AdminSite):
    site_header = 'My custom header'

blog = BlogAdmin(name='Blog App Section')


blog.register(Blog)
admin.site.register(Blog)