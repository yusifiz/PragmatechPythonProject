from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Main info..')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=63, verbose_name='Muellif',null=True,blank=True)
    slug = models.SlugField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.slug])
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('created_at',)

    def __str__(self):
        return self.title
        