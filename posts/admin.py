from django.contrib import admin
from posts.models import Post, PostImage, Comment
import admin_thumbnails

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "content",]
    inlines = [CommentInline, PostImageInline]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "photo",]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "content",]







# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "content",]
#     list_display_links = ["post",]
#     search_fields = ["content",]


# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     list_display = ["id", "post", "photo",]
#     list_display_links = ["post",]
#     search_fields = ["post",]

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["id", "post", "user", "content", "created_at",]
#     list_display_links = ["post",]
#     search_fields = ["content",]