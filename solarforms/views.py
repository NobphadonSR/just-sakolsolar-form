from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import SolarDataForms
from .models import SolarDatas
import pandas as pd
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

def salorformpage(request):
    if request.method == 'POST':
        form = SolarDataForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว')
            return redirect('solarform')
    else:
        form = SolarDataForms()
    
    context = {
        'form': form,
    }
    
    # เพิ่มข้อมูลสำหรับแอดมิน
    if request.user.is_staff:
        context['solar_data'] = SolarDatas.objects.all().order_by('-created_at')
    
    return render(request, 'solarforms/solarforms.html', context)

@staff_member_required
def export_excel(request):
    # ดึงข้อมูลทั้งหมด
    solar_data = SolarDatas.objects.all()
    
    # แปลงข้อมูลเป็น list of dictionaries และแปลง timezone
    data_list = []
    for data in solar_data:
        data_dict = {
            'ชื่อสถานที่': data.location_name,
            'ชื่อผู้ติดต่อ': data.contact_name,
            'เบอร์โทรศัพท์': data.phone_number,
            'ช่วงเวลาที่สะดวกในการติดตั้ง': data.preferred_contact_date,
            'วันที่สะดวกในการสำรวจหน้างาน': data.preferred_survey_date,
            'ค่าไฟฟ้าเดือนล่าสุด': data.latest_electric_bill,
            'ข้อมูลที่อยากระบุเพิ่มเติม': data.additional_info,
            'วันที่ลงทะเบียน': timezone.localtime(data.created_at).replace(tzinfo=None)
        }
        data_list.append(data_dict)
    
    # สร้าง DataFrame
    df = pd.DataFrame(data_list)
    
    # สร้าง response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="solar_data.xlsx"'
    
    # บันทึกเป็น Excel
    df.to_excel(response, index=False)
    return response