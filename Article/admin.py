from django.contrib import admin

# Register your models here.
from .models import Post
from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
# admin.site.register(Entry)

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'publish', 'approved_comments','author')
    list_filter   = ('publish',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']
    fieldsets = ((None,
                  {'fields': ('title', 'slug', 'body', 'image',
                              'approved_comments', 'publish', 'author',)}),)
    readonly_fields = ('publish',)
    # summernote_fields = ('body',)


admin.site.register(Post, PostAdmin)
