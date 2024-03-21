from django.contrib import admin

from .models import GameCategoryModel, GameModel


@admin.register(GameCategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["game_category_title", "created_at"]
    search_fields = ["game_category_title"]
    list_filter = ["created_at"]
    ordering = ["game_category_title"]


@admin.register(GameModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["game_title", "game_price", "game_created_at"]
    search_fields = ["game_title"]
    list_filter = ["game_created_at"]
    ordering = ["game_title"]


