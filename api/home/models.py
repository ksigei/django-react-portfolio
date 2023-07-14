from django.db import models

# contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return 'Message {} by {}'.format(self.content, self.name)
    
    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']

# newsletter
class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return 'Email {}'.format(self.email)
    
    class Meta:
        verbose_name_plural = 'Newsletters'
        ordering = ['-created_at']

# about
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='about', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return 'About {}'.format(self.title)
    
    class Meta:
        verbose_name_plural = 'Abouts'
        ordering = ['-created_at']

# social media
class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    icon = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return 'Social Media {}'.format(self.name)
    
    class Meta:
        verbose_name_plural = 'Social Medias'
        ordering = ['-created_at']

