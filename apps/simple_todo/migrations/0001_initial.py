# Generated by Django 4.0.3 on 2022-03-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('P', 'Personal'), ('S', 'Shopping'), ('W', 'Wishlist'), ('O', 'Office'), ('C', 'Custom')], max_length=1)),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('remainder', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('finised', models.BooleanField(default=False)),
            ],
        ),
    ]
