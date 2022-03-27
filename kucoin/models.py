from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import truncatechars
from extensions.utils import jalali_converter
from django.template.defaultfilters import truncatechars
from django_jalali.db import models as jmodels









#------------------------------------------------------------------------------
class Item(models.Model):
    available = models.BooleanField(default=True, verbose_name = "قابل مشاهده در سایت" )
    code = models.CharField(max_length=200, unique=True, verbose_name = "کد فایل")
    CHOICES1 = ( ('رهن و اجاره','رهن و اجاره'), ('رهن کامل','رهن کامل'), ('فروش','فروش'), ('پیش فروش','پیش فروش') )
    buy_status = models.CharField(max_length=30,choices=CHOICES1,verbose_name = "نوع معامله")
    CHOICES2 = ( ('آپارتمان','آپارتمان'), ('خانه ویلایی','خانه ویلایی'), ('زمین','زمین'), ('مغازه و تجاری','مغازه و تجاری'), ('دفتر کار اداری','دفتر کار اداری'), ('کلنگی','کلنگی'), ('ویلا','ویلا'), ('باغ','باغ') )
    estate_status = models.CharField(max_length=30,choices=CHOICES2,verbose_name = "نوع ملک")
    area_size = models.IntegerField(null=True,blank=True, verbose_name = "متراژ (متر)")
    room_qty = models.IntegerField(null=True,blank=True, verbose_name = "تعداد اتاق")
    building_age = models.IntegerField(null=True,blank=True, verbose_name = "سن بنا (سال)")
    parking = models.BooleanField(default=False, verbose_name = "پارکینگ" )
    storage_room = models.BooleanField(default=False, verbose_name = "انباری" )
    elevator = models.BooleanField(default=False, verbose_name = "آسانسور" )
    balcony = models.BooleanField(default=False, verbose_name = "بالکن" )
    deposit = models.IntegerField(null=True,blank=True, default='0', verbose_name = "ودیعه (تومان)")
    rent = models.IntegerField(null=True,blank=True, default='0', verbose_name = "اجاره (تومان)")
    price = models.IntegerField(null=True,blank=True, default='0', verbose_name = "قیمت فروش (تومان)")
    area = models.ForeignKey(Area, on_delete=models.CASCADE,verbose_name = "منطقه")
    additional_information = models.TextField(max_length=2000,null=True, blank=True,verbose_name = "اطلاعات تکمیلی")
    date = jmodels.jDateTimeField(auto_now_add=True, verbose_name = "تاریخ آگهی")
    image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")
    video_link = models.URLField(max_length=500, null=True, blank=True, verbose_name = "لینک ویدئو")
    sales_expert = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE,verbose_name = "کارشناس فروش")
    ownership = models.ForeignKey(Ownership, null=True,blank=True, on_delete=models.CASCADE,verbose_name = "مالکیت")


    class Meta:
        verbose_name = "ملک"
        verbose_name_plural = "املاک"

    def __str__(self):
        return str(self.buy_status +" "+ self.estate_status +" در "+ self.area.name )

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))

    def get_absolute_url(self):
        return reverse('app:items_detail',args=[self.id])

    def get_absolute_crm_url(self):
        return reverse('crm_items_detail',args=[self.id])

    def get_absolute_edit_url(self):
        return reverse('crm_item_edit',args=[self.id])







# End
