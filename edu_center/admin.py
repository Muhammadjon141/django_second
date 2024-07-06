from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Book, Authors, User, Comments



@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'author_full_name')
    list_display_links = ('title', 'author_full_name')
    ordering = ('title', )
    search_fields = ('title', 'author_full_name')
    propulated_fields = ('title', )

    def author_full_name(self, obj):
        return obj.author.full_name()
    
    
    

@admin.register(Authors)
class AuthorsAdmin(ImportExportActionModelAdmin):
    values = ('first_name',)
    values_list = ('first_name', )
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
    ordering = ('first_name', )
    search_fields = ('first_name',)
    propulated_fields = ('first_name', )


    def author_full_name(self, obj):
        return obj.author.full_name()
    
@admin.register(User)
class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Comments)
class CommentsAdmin(ImportExportActionModelAdmin):
    list_display = ('comment',)