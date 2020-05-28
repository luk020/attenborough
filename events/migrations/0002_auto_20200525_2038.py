# Generated by Django 3.0.6 on 2020-05-26 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='episode_id',
        ),
        migrations.AddField(
            model_name='event',
            name='episode',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='show_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.Show'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='eps',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
    ]