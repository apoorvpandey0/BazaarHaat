# Generated by Django 3.0.2 on 2020-06-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New market', max_length=50)),
                ('description', models.TextField(default='Yaha sab milta hai bhai')),
                ('city', models.CharField(default='Bhopal', max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='markets')),
            ],
        ),
    ]
