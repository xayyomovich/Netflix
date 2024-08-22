# Generated by Django 5.0.6 on 2024-06-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_actor_movie_movie_casted_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='casted_actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='casted_actors',
            field=models.ManyToManyField(related_name='movies', to='movies.actor'),
        ),
    ]
