# Generated by Django 5.0.6 on 2024-06-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='market_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='market',
            old_name='market_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='market',
            old_name='market_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='market',
            old_name='market_phone',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='market',
            name='Tax_id',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='market',
            name='password',
            field=models.CharField(default='default_password_value', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='product_stocks',
            field=models.IntegerField(default=0),
        ),
    ]