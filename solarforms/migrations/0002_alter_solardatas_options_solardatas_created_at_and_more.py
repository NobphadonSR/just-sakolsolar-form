# Generated by Django 5.1.3 on 2025-01-15 04:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solardatas',
            options={'verbose_name': 'ข้อมูลผู้สนใจติดตั้งโซลาร์', 'verbose_name_plural': 'ข้อมูลผู้สนใจติดตั้งโซลาร์'},
        ),
        migrations.AddField(
            model_name='solardatas',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solardatas',
            name='location_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ชื่อสถานที่'),
        ),
        migrations.AlterField(
            model_name='solardatas',
            name='preferred_survey_date',
            field=models.DateField(blank=True, null=True, verbose_name='วันที่สะดวกให้สำรวจหน้างาน'),
        ),
    ]
