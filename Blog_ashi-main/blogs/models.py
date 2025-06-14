from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Supported extensions are: {", ".join(valid_extensions)}')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatars/', blank=False, null=False, validators=[validate_file_extension])
    description = models.CharField(max_length=512, blank=False, null=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profile'


class Article(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    cover = models.FileField(upload_to='files/article_covers/', blank=False, null=False, validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)


class Category(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    cover = models.FileField(upload_to='files/category_covers/', blank=False, null=False, validators=[validate_file_extension])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
