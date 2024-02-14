# Generated by Django 5.0 on 2024-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('amount', models.FloatField()),
                ('oldbalanceOrg', models.FloatField()),
                ('newbalanceOrig', models.FloatField()),
                ('oldbalanceDest', models.FloatField()),
                ('newbalanceDest', models.FloatField()),
                ('isFraud', models.BooleanField()),
            ],
        ),
    ]