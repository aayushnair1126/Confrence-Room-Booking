# Generated by Django 3.1.6 on 2021-05-27 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.CharField(max_length=100)),
                ('book_price', models.CharField(max_length=3)),
                ('genre', models.CharField(max_length=15)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pracapp.book')),
            ],
        ),
    ]
