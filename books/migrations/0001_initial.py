# Generated by Django 4.0.3 on 2022-05-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('publisher', models.TextField(null=True)),
                ('published_date', models.DateField(null=True)),
                ('average_rating', models.FloatField(null=True)),
                ('authors', models.ManyToManyField(to='books.bookauthor')),
                ('categories', models.ManyToManyField(to='books.category')),
            ],
        ),
    ]
