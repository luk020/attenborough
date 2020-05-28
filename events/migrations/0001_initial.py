# Generated by Django 3.0.6 on 2020-05-26 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep_number', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField(max_length=4)),
                ('eps', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=32)),
                ('continent', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('time', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('episode_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.Episode')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='events.Show'),
        ),
    ]
