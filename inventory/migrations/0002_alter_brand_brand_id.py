# Generated by Django 4.2.3 on 2024-02-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
