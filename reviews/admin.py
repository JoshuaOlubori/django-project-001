from django.contrib import admin
from reviews.models import (Publisher,  Contributor, Book, BookContributor, Review)

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn']
    list_filter = ['publisher', 'publication_date']
    search_fields = ['title', 'isbn']
    date_hierarchy = 'publication_date'

@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['last_names', 'first_names']
    list_filter = ['last_names']
    search_fields = ['last_names__startswith', 'first_names']

admin.site.register(Publisher)
admin.site.register(BookContributor)
admin.site.register(Review)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               