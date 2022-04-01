from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse








#------------------------------------------------------------------------------
class Exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    name = models.CharField(max_length=80, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    api_passphrase = models.CharField(max_length=100)
    CHOICES = ( ('فعال','فعال '),('غیرفعال','غیرفعال '))
    status = models.CharField(max_length=30,choices=CHOICES, default='فعال', verbose_name = "وضعیت")

    def get_absolute_url(self):
        return reverse('exchange',args=[self.id])

    def __str__(self):
        return str(self.name)

    class Meta:
      verbose_name = "صرافی"
      verbose_name_plural = "صرافی ها"














#End
