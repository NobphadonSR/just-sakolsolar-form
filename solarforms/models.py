from django.db import models

class SolarDatas(models.Model):
    location_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='ชื่อสถานที่')
    contact_name = models.CharField(max_length=100, verbose_name='ชื่อผู้ติดต่อ')
    phone_number = models.CharField(max_length=20, verbose_name='เบอร์โทรศัพท์ติดต่อ')
    preferred_contact_time = models.TimeField(null=True, blank=True, verbose_name='เวลาที่สะดวกให้ติดต่อ')
    preferred_survey_date = models.DateField(null=True, blank=True, verbose_name='วันที่สะดวกให้สำรวจหน้างาน')
    latest_electric_bill = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='ค่าไฟฟ้าเดือนล่าสุด')
    additional_info = models.TextField(blank=True, null=True, verbose_name='ข้อมูลที่อยากระบุเพิ่มเติม')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ข้อมูลผู้สนใจติดตั้งโซลาร์"
        verbose_name_plural = "ข้อมูลผู้สนใจติดตั้งโซลาร์"

    def __str__(self):
        return f"{self.location_name} - {self.contact_name}"