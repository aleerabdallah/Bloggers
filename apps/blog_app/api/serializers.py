from rest_framework import serializers
from ..models import Post, Category, Tag 







class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


    # title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(null=False, unique=True, max_length=200)
    # author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts")
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="posts")
    # tags = models.ManyToManyField('Tag', blank=True)
    # image = ResizedImageField(null=True, blank=True)
    # description = models.CharField(max_length=255, blank=True, null=True)
    # summary = models.TextField(blank=True, null=True)
    # body = HTMLField(blank=True, null=True)
    # status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=DRAFT)
    # published_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category', 'tags', 'image', 'description', 'summary', 'body']
