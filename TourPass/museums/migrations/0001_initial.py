# Generated by Django 5.1.4 on 2024-12-28 01:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('opening_hour', models.CharField(max_length=100)),
                ('image_location', models.CharField(blank=True, max_length=200, null=True)),
                ('price_per_ticket', models.DecimalField(blank=True, decimal_places=2, help_text='In units of currency, e.g., INR.', max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('total_tickets', models.PositiveBigIntegerField()),
                ('remaining_tickets', models.PositiveBigIntegerField()),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='museums.museum')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='museums.museum')),
                ('timeslot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='museums.timeslot')),
            ],
        ),
    ]
