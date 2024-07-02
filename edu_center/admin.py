from django.contrib import admin
from .models import Book, Authors, User, Comments
# Register your models here.
# book = Book[1]
# author = Authors[1]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # search_fields = ('title', 'author__name')
    # list_filter = ('create_date', 'author')

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(User)
admin.site.register(Comments)