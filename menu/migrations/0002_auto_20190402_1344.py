# Generated by Django 2.1.7 on 2019-04-02 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_category_name', models.CharField(max_length=200)),
                ('ingredient_category_image', models.TextField()),
                ('ingredient_category_des', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='menu.Ingredientcategory'),
        ),
    ]
