from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                                        .filter(status='published')



class Post (models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    
    objects = models.Manager()
    published1 = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.pk])

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title



# Create your models here.
