from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    image = ResizedImageField(blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)




class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse




class Post(models.Model):
    PUBLISHED = "p"
    DRAFT = "d"
    WITHDRAWN = "w"
    FUTURE = "f"

    STATUS_CHOICES = (
        (PUBLISHED, "Published"),
        (DRAFT, "Draft"),
        (WITHDRAWN, "Withdrawn"),
        (FUTURE, "Future")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=200)
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")
    image = ResizedImageField(size=[600, 600], quality=85, upload_to="Techbros/Post_Thumbnails")
    description = models.CharField(max_length=255)
    summary = models.TextField()
    body = HTMLField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=DRAFT)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-published_on',)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse('post')

    @property
    def get_image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    # @get_related_posts_by_category


    # get_comments






