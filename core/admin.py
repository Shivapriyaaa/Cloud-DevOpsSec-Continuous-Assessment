from django.contrib import admin

from .models import BlogPost, Comment, Like, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__username", "bio", "location")
    filter_horizontal = ("following",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at")
    search_fields = ("author__username", "post__title", "content")
    list_filter = ("created_at",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user__username", "post__title")
    list_filter = ("created_at",)


