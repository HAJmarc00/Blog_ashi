from django.contrib import admin
from .models import UserProfile, Article, Category

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'description')
    search_fields = ('user__username', 'description')
    list_filter = ('user__is_active',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'content', 'category')
    search_fields = ('title', 'author__user__username')
    list_filter = ('created_at', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)