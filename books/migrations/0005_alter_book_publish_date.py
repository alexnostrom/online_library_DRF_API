# Generated by Django 4.2.5 on 2023-09-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_review_options_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.IntegerField(verbose_name='Дата публикации'),
        ),
    ]
