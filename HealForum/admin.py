from django.contrib import admin

# Register your models here.
from HealForum.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'post_date', 'created_by']
    filter_horizontal = ['likes']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'description_comment', 'comment_date', 'commented_by']
    filter_horizontal = ['likes']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
