from django.conf import settings
from django.db import models


# Create your models here.

STATUS = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
    ('Disabled', 'Disabled'),
)

USER_ROLES = (
    ('Admin', 'Admin'),
    ('Publisher', 'Publisher'),
)

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField(max_length=2048)
    post_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    edit_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts')
    likes = models.ManyToManyField(User, related_name="post_likes")

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.ForeignKey(Post, related_name='comment', blank=True, null=True)
    description_comment = models.TextField(max_length=2048, blank=True, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    edit_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='commented_by', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True, null=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def get_comments(self):
        return self.objects.all()

    def __str__(self):
        return 'Commetn object'
