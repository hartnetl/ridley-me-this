# Generated by Django 3.2 on 2022-01-10 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchandise', '0004_delete_turtles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turtle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('turtle_id', models.CharField(max_length=6)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('species', models.CharField(choices=[('logger', 'Loggerhead'), ('green', 'Green'), ('leather', 'Leatherback'), ('flat', 'Flatback'), ('hawks', 'Hawksbill'), ('olive', 'Olive Ridley'), ('kemp', "Kemp's Ridley")], max_length=10)),
                ('description', models.TextField()),
                ('date_tagged', models.DateField()),
                ('location_tagged', django_countries.fields.CountryField(max_length=2)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sponsored_status', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchandise.category')),
            ],
            options={
                'verbose_name_plural': 'Turtles',
            },
        ),
        migrations.CreateModel(
            name='turtle_sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sponsorship_start', models.DateField()),
                ('sponsorship_end', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchandise.category')),
                ('sponsored_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('turtle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='turtles.turtle')),
            ],
            options={
                'verbose_name_plural': 'Turtle Sponsorships',
            },
        ),
    ]
