# Generated by Django 5.0.6 on 2024-06-24 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_remove_car_image_remove_car_price_car_availability_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=30)),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='MyApp.car')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]