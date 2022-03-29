# Generated by Django 2.2 on 2022-03-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]