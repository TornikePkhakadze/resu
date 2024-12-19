from django.contrib import admin
from shop.models import Category , Item, Tag
from shop.filter import PriceFilter


# class ItemInline(admin.TabularInline):
#     model = Item
#     extra =1

class ItemInline(admin.StackedInline):
    model = Item
    extra =1
    
class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1

# class ItemInline(admin.StackedInline):
#     model = Category..through 
#     extra = 1

class TagItemInline(admin.TabularInline):
    model = Tag.items.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","get_five_items"]
    search_fields = ["name", "items__name"]
    ordering = ["id"]
    list_per_page = 100
    inlines = [ItemInline]

    def get_five_items(self,category):
        return[racginda.name for racginda in category.items.all()[:5]]
    
    def get_queryset(self, request):
        existing_queriset = super().get_queryset(request)
        return existing_queriset.prefetch_related("items")    
                 
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id","name","price"]
    search_fields = ["name"]
    ordering = ["price"]
    fields = ["name","price","category","description"]
    autocomplete_fields = ["category"]
    inlines  = [TagInline]
    list_filter = [PriceFilter]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    inlines = [TagInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Item,ItemAdmin)