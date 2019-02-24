from django.contrib import admin

from . import models


@admin.register(models.NewsSite)
class NewsSiteAdmin(admin.ModelAdmin):
    list_display = ("name", "rss_url")
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "published", "site")
    ordering = ("title", "site")
    search_fields = ("title", "site")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "site")
    ordering = ("name", "site")
    search_fields = ("name", "site")
