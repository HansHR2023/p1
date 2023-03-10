# Generated by Django 4.1.5 on 2023-03-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netlify',
            name='alcohol',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='exercise',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='genetic',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='length',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='lifespan',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='mass',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='smoking',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='netlify',
            name='sugar',
            field=models.FloatField(null=True),
        ),
    ]
