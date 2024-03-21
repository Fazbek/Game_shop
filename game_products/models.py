from django.db import models


class GameCategoryModel(models.Model):
    game_category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game_category_title

    class Meta:
        verbose_name = "Game category"
        verbose_name_plural = "Game categories"


class GameModel(models.Model):
    game_title = models.CharField(max_length=50, help_text="Here add name of product")
    game_category = models.ForeignKey(GameCategoryModel, on_delete=models.CASCADE)
    game_price = models.FloatField()
    game_count = models.IntegerField()
    game_descriptions = models.TextField()
    game_image = models.FileField(upload_to="product_images")
    game_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game_title

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"




