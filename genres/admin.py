from django.contrib import admin
from genres.models import Genre

# Admin do carro
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'name',
        'timestamp',
        'description',
        
    )
    list_filter = (
        'id',
        'name',
        'timestamp',
    )
    search_fields = (
        'id',
        'name',
        'timestamp',
    )
    ordering = ('-id',)    
    readonly_fields = ('id',)
