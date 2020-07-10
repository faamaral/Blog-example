from django.contrib import admin
from . models import Post, Category

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'published')
    list_filter = ('name', 'created', 'published')
    date_hierarchy = 'published'
    search_fields = ('name',)

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','published','status')
    list_filter = ('status','published','created','author')
    readonly_fields = ('show_img',)
    raw_id_fields = ('author',)
    date_hierarchy = ('published')
    search_fields = ('title','content')
    prepopulated_fields = {'slug':('title',)}

    def show_img(self, obj):
        return obj.view_image

    show_img.short_description = "Picture has been cadastred"
