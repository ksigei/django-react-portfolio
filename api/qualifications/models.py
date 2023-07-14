from django.db import models
import uuid
# tagulous
from tagulous.models import TagField

class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['-id']


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.school
    
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-id']


class Skill(models.Model):
    # proficiency choices
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    proficiency = models.CharField(choices=PROFICIENCY_CHOICES, max_length=200)
    tags = TagField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-id']


class Project(models.Model):
    # project type choices
    PROJECT_TYPE_CHOICES = [
        ('Personal', 'Personal'),
        ('Academic', 'Academic'),
        ('Open Source', 'Open Source'),
        ('Freelance', 'Freelance'),
        ('Hackathon', 'Hackathon'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Volunteer', 'Volunteer'),
        ('Professional', 'Professional'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=200)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-id']

# achievements
class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Achiement'
        verbose_name_plural = 'Achievements'
        ordering = ['-id']

# certifications
class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['-id']

# awards
class Award(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
        ordering = ['-id']

# publications
class Publication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-id']

# languages
class Language(models.Model):
    # proficiency choices
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    proficiency = models.CharField(choices=PROFICIENCY_CHOICES, max_length=200)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['-id']

# interests
class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'
        ordering = ['-id']

# hobbies
class Hobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
        ordering = ['-id']


# references
class Reference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'
        ordering = ['-id']

# resume
class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/resumes/', null=True, blank=True)
    tags = TagField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'




