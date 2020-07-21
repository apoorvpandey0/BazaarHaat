# Generated by Django 3.0.2 on 2020-06-09 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', help_text='Designates the users Profile picture.', upload_to='profile_pics', verbose_name='Profile Picture')),
                ('address_line1', models.CharField(help_text='Designates the users Address line1.', max_length=100, verbose_name='Address line 1')),
                ('address_line2', models.CharField(help_text='Designates the users Address line 2.', max_length=100, verbose_name='Address line 2')),
                ('pincode', models.CharField(help_text='Designates the users PINCODE.', max_length=6, verbose_name='Pincode')),
                ('contactno', models.CharField(default=1234567890, max_length=10)),
                ('is_seller', models.BooleanField(default=False, help_text='Designates whether the user has a seller account or not.', verbose_name='Seller status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
