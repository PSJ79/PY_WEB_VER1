from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'create_date', 'modify_date')

admin.site.register(Post, PostAdmin)