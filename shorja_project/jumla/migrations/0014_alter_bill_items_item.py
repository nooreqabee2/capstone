# Generated by Django 4.0.4 on 2022-06-10 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jumla', '0013_rename_available_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_items',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_item', to='jumla.product'),
        ),
    ]
