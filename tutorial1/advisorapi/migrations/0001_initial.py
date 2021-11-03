# Generated by Django 3.2.8 on 2021-11-03 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('adName', models.CharField(max_length=100)),
                ('adProfilePictureURL', models.TextField()),
                ('adId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdvisorBookingTrans',
            fields=[
                ('bookingId', models.AutoField(primary_key=True, serialize=False)),
                ('bookingDateTime', models.DateTimeField()),
                ('whichAdvisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapi.advisor')),
                ('whoBooked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='AdvisorBooking',
            fields=[
                ('bookingId', models.AutoField(primary_key=True, serialize=False)),
                ('bookingDateTime', models.DateTimeField()),
                ('whichAdvisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapi.advisor')),
                ('whoBooked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapi.user')),
            ],
        ),
    ]
