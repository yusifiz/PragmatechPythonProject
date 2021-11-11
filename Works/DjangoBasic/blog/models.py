from django.db import models
from django.urls import reverse
from django.utils.text  import slugify
import string,random
from django.db.models.signals import pre_save
from core.utils import  unique_slug_generator
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    
class Blog(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Main info..')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=63, verbose_name='Muellif',null=True,blank=True)
    slug = models.SlugField(max_length=255, null=True,unique=True,blank=True)
    image = models.ImageField(upload_to="blog/", null=True)



    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.slug])
    
    
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('created_at',)

    def __str__(self):
        return self.title
    

def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
            
pre_save.connect(slug_generator, sender=Blog)