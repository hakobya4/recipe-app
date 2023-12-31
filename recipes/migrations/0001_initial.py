# Generated by Django 4.2.6 on 2023-11-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('adapted', models.CharField(max_length=120)),
                ('adapted_link', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('direction', models.CharField(max_length=10000)),
                ('prepTime', models.PositiveIntegerField()),
                ('cookTime', models.PositiveIntegerField()),
                ('totalTime', models.PositiveIntegerField()),
                ('serving', models.PositiveIntegerField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('intermediate', 'Intermediate'), ('hard', 'Hard')], default='easy', max_length=12)),
                ('ingredients', models.CharField(max_length=1000)),
                ('pic', models.ImageField(default='no_picture.jpg', upload_to='recipes')),
            ],
        ),
    ]
