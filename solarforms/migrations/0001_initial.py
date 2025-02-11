# Generated by Django 5.1.3 on 2025-01-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200, null=True, verbose_name='ชื่อสถานที่')),
                ('contact_name', models.CharField(max_length=100, verbose_name='ชื่อผู้ติดต่อ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='เบอร์โทรศัพท์ติดต่อ')),
                ('preferred_contact_date', models.DateField(verbose_name='วันที่สะดวกให้ติดต่อ')),
                ('preferred_survey_date', models.DateField(null=True, verbose_name='วันที่สะดวกให้สำรวจหน้างาน')),
                ('latest_electric_bill', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ค่าไฟฟ้าเดือนล่าสุด')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='ข้อมูลที่อยากระบุเพิ่มเติม')),
            ],
        ),
    ]
