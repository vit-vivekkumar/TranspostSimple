from django.contrib import admin
from .models import Post, Comment, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_on', 'upload')
    search_fields = ['content']
    list_filter = ('created_on',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author__username', 'content')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user__username',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)