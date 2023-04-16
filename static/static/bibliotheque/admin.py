from django.contrib import admin
from .models import Book,Category

# Register your models here.
# admin.site.register([Book,Category])

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "manager",
        "autor",
        "body",
        "image",
        "avaible",
        "exemplaire",
        "tag"
    )

    list_editable=("autor","avaible","exemplaire","body","image","tag")
    search_fields=("title","autor")
    list_filter=("avaible","tag")
    autocomplete_fields=("manager","category",)
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=("label","slug")
    prepopulated_fields={"slug":("label",)}

