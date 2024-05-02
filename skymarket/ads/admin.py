from django.contrib import admin

from ads.models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
# admin.site.register(Ad)
# admin.site.register(Comment)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'price', 'created_at')
    list_filter = ('author', 'title',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('pk', 'ad', 'author', 'text', 'created_at')
    list_filter = ('author',)
