from django.db import models
from django.urls import reverse
from django.utils.text  import slugify
import string,random
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



    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Blog,self).save(*args,**kwargs)
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('created_at',)

    def __str__(self):
        return self.title
        