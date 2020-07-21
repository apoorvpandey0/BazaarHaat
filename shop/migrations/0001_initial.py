# Generated by Django 3.0.2 on 2020-06-09 16:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('pages', '0001_initial'),
        ('market', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Mohan supermart', help_text='This is the name of your shop/bussiness as in GSTIN registration.', max_length=50, verbose_name='Name of your shop')),
                ('GSTIN', models.CharField(max_length=15, unique=True, verbose_name='GSTIN Number')),
                ('address_line1', models.CharField(help_text='Designates the Address line1 of the Shop.', max_length=100, verbose_name='Address line 1')),
                ('address_line2', models.CharField(help_text='Designates the Address line 2 of the Shop.', max_length=100, verbose_name='Address line 2')),
                ('pincode', models.CharField(help_text='Designates the users PINCODE.', max_length=6, verbose_name='Pincode')),
                ('contact_person', models.CharField(help_text='Person to contact to for proceeding with the approval process.', max_length=40, verbose_name='Contact person.')),
                ('status', models.BooleanField(default=False, help_text='Designates the approval status of the shop.', verbose_name='Approved')),
                ('description', models.CharField(default='We sell the products you love :)', help_text='A sweet little description about your shop.', max_length=200)),
                ('shopno', models.IntegerField(default=1, help_text='Shop number in your market.')),
                ('contactno', models.CharField(default='9786756453', help_text='A contact number', max_length=10)),
                ('image', models.ImageField(default='default.png', help_text='Please select a picture of your shop.', upload_to='static/shops')),
                ('pub_ratings', models.IntegerField(blank=True, default=0)),
                ('category', models.ForeignKey(help_text='Category your shop belongs to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Category')),
                ('market', models.ForeignKey(help_text='The market in which your shop is located in.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.Market')),
                ('owner', models.OneToOneField(help_text='Please select the profile of the owner of this shop.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile')),
            ],
        ),
    ]
