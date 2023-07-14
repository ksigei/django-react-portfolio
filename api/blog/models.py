from django.db import models
import uuid
from django.contrib.auth.models import User
# django tagging
from tagulous.models import TagField


# ckeditor
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='media/category', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

# post files
def post_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'media/post/%s' % (filename)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField()
    featured_image = models.ImageField(upload_to=post_file_name, null=True, blank=True)
    post_files = models.ImageField(upload_to=post_file_name, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TagField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    heart = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title
    
    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

# comment
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):

        return 'Comment {} by {}'.format(self.content, self.name)
    
    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

# reply
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):

        return 'Reply {} by {}'.format(self.content, self.name)
    
    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ['-created_at']











