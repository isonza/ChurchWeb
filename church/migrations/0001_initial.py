# Generated by Django 3.1.6 on 2021-06-16 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerTestimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_or_prayer', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('devotee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.devotee')),
            ],
        ),
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='NOT-ALLOWED', max_length=20)),
                ('COVID_INTERACTION', models.CharField(max_length=20)),
                ('HAVE_FEVER', models.CharField(max_length=20)),
                ('OUTSIDE_TRAVEL', models.CharField(max_length=20)),
                ('AREA', models.CharField(max_length=20)),
                ('devotee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.devotee')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatNumber', models.CharField(max_length=500)),
                ('service', models.CharField(max_length=200)),
                ('totalSeat', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('attendee', models.CharField(max_length=500, null=True)),
                ('bookingDate', models.DateField(auto_now=True)),
                ('devotee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.devotee')),
            ],
        ),
    ]