from django.shortcuts import render
from game_products.models import GameCategoryModel, GameModel


def home_page(request):
    game_categories = GameCategoryModel.objects.all()
    game_products = GameModel.objects.all()
    context = {"game_categories": game_categories, "game_products": game_products}
    return render(request, template_name="index.html", context=context)

