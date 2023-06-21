# Generated by Django 3.2 on 2023-06-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0006_rename_ingredient_recipeingredient_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.IntegerField(verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=20, verbose_name='цветовой hex'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(
                max_length=200, verbose_name='название тэга'
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(
                max_length=200, verbose_name='текстовый слаг тэга'
            ),
        ),
        migrations.AddConstraint(
            model_name='favourite',
            constraint=models.UniqueConstraint(
                fields=('owner', 'recipes'), name='unique_favorite'
            ),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(
                fields=('author', 'follower'), name='unique_follow'
            ),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(
                fields=('owner', 'recipes'), name='unique_shopping_cart'
            ),
        ),
    ]