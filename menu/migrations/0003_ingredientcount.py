# Generated by Django 2.1.7 on 2019-03-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_foodchoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_count', models.IntegerField()),
                ('ingredient_count_des', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingredient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Ingredient')),
            ],
        ),
    ]