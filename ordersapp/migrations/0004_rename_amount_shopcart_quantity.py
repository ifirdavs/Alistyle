# Generated by Django 4.1 on 2022-10-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0003_alter_shopcart_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='amount',
            new_name='quantity',
        ),
    ]
