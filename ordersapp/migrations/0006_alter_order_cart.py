# Generated by Django 4.1 on 2022-11-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(related_name='order_carts', to='ordersapp.shopcart'),
        ),
    ]
