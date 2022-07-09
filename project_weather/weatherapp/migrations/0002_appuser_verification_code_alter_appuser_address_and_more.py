# Generated by Django 4.0.4 on 2022-07-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='verification_code',
            field=models.CharField(default='0', max_length=8),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherapp.appuser'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='weather_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherapp.weathertype'),
        ),
    ]
