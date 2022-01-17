from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):

        fullname = models.CharField(_("نام و نام خانوادگی"), max_length=150 , blank=True,null=True)
        course = models.CharField(_("رشته"), max_length=100, blank=True,null=True)
        uniid = models.CharField(_("کد دانشجویی"), max_length=50,unique=True, blank=True,null=True)
        entered = models.CharField(_("سال ورود"), max_length=50, blank=True,null=True)
        mobile = models.CharField(_("شماره موبایل"), max_length=50, unique=True, blank=True,null=True)
        invitecode = models.CharField(_("کد دعوت"), max_length=50, blank=True,null=True)
        submited = models.CharField(_("تعداد ثبت نام شده"), max_length=50, blank=True,null=True)
        create_at = models.DateTimeField(_("زمان ثبت نام"), auto_now=True, blank=True,null=True)
        bed = models.CharField(_("خوابگاهی؟"), max_length=50, blank=True,null=True)

class Capacity(models.Model):

        submited = models.CharField(_("تعداد ثبت نام شده"), max_length=50, blank=True,null=True)