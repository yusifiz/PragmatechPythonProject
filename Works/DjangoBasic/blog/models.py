from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Main info..')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=63, verbose_name='Muellif',null=True,blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('created_at',)

    def __str__(self):
        return self.title
        