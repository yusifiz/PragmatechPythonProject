from django.contrib import admin

# Register your models here.

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    site_header = 'My custom header'
    fields = ('title','text','author','image',)

# blog = BlogAdmin(name='Blog App Section')


# blog.register(Blog)
# admin.site.register(Blog)