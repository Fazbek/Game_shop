from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from game_products.models import GameCategoryModel, GameModel
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def home_page(request):
    game_categories = GameCategoryModel.objects.all()
    game_products = GameModel.objects.all()
    context = {"game_categories": game_categories, "game_products": game_products}
    return render(request, template_name="index.html", context=context)


class MyLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/"


def logout_view(request):
    logout(request)
    return redirect("home")


def create(request, pk):
    game_create = GameModel.objects.get(pk=pk)
    if request.method == "POST":
        game_create.game_title = request.POST.get("game_title")
        game_create.game_descriptions = request.POST.get("game_descriptions")
        game_create.game_image = request.POST.get("game_image")
        game_create.game_created_at = request.POST.get("game_created_at")
        game_create.save()
        game_create.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "create.html", {"game_create": game_create})


def edit(request, pk):
    try:
        game_edit = GameModel.objects.get(pk=pk)

        if request.method == "POST":
            game_edit.game_title = request.POST.get("game_title")
            game_edit.game_descriptions = request.POST.get("game_descriptions")
            game_edit.game_image = request.POST.get("game_image")
            game_edit.game_created_at = request.POST.get("game_created_at")
            game_edit.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"game_edit": game_edit})
    except GameModel.DoesNotExist:
        return HttpResponseNotFound("<h2>Game not found</h2>")


def delete(request, pk):
    try:
        game_delete = GameModel.objects.get(pk=pk)
        game_delete.delete()
        return HttpResponseRedirect("/")
    except GameModel.DoesNotExist:
        return HttpResponseNotFound("<h2>Game not found</h2>")

