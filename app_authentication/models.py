from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import truncatechars





#------------------------------------------------------------------------------
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,related_name='profile',verbose_name = "کاربر")
  phone = models.CharField(max_length=50,null=True, blank=True,verbose_name="شماره تماس")
  photo = models.ImageField(default='default.png', upload_to='profile_pics', null=True, blank=True, verbose_name = "تصویر")

  def __str__(self):
      return str(self.user)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  def get_absolute_url(self):
      return reverse('user_detail',args=[self.id])

  def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.photo.url))

  class Meta:
      verbose_name = "کاربر"
      verbose_name_plural = "کاربران"












#------------------------------------------------------------------------------
class Exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    name = models.CharField(max_length=80, verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    api_passphrase = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('exchange',args=[self.id])

    def __str__(self):
        return str(self.name)

    class Meta:
      verbose_name = "صرافی"
      verbose_name_plural = "صرافی ها"













#End
