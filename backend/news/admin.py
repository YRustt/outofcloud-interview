from django.contrib import admin

from . import models


@admin.register(models.NewsSite)
class NewsSiteAdmin(admin.ModelAdmin):
    list_display = ("name", "rss_url")
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("site", "title", "link", "published")
    ordering = ("site", "title")
    search_fields = ("title", "site__name")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("site", "name")
    ordering = ("site", "name")
    search_fields = ("name", "site__name")
