from django.contrib import admin
from .models import Ingredient, Recipe, IngredientInRecipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "measurement_unit")
    search_fields = ("name",)
    list_filter = ("measurement_unit",)


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 1
    autocomplete_fields = (
        "ingredient",
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "cooking_time", "pub_date")
    search_fields = ("name", "author__username", "text")
    list_filter = ("author", "pub_date")
    inlines = [IngredientInRecipeInline]
    readonly_fields = ("pub_date",)

    fieldsets = (
        (None, {"fields": ("name", "author", "text", "image")}),
        (
            "Детали рецепта",
            {
                "fields": ("cooking_time",)
            },
        ),
        ("Даты", {"fields": ("pub_date",), "classes": ("collapse",)}),
    )
