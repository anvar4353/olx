# Generated by Django 4.1 on 2022-11-03 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_menu_options_menu_create_menu_moder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpost',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.menu'),
        ),
    ]
