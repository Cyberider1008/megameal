# Generated by Django 5.2.3 on 2025-07-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount_type', models.CharField(choices=[('flat', 'Flat'), ('percent', 'Percentage')], max_length=10)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('min_order_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
