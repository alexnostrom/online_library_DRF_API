# Generated by Django 4.2.5 on 2023-09-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
