import os
import urllib
from django.db import models
from django.conf import settings
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Spice_Login(models.Model):
    spice_user_name=models.TextField(verbose_name='User_Name',max_length=125,null=False,blank=False)
    spice_user_password=models.TextField(verbose_name='Password',max_length=125,null=False,blank=False)


    class Meta:
        verbose_name_plural = 'Spice_Login'
        verbose_name = 'Spice_Login'
        db_table = 'spice_login'

    def __unicode__(self):
        return "{}:".format(self.spice_user_name)


class View_Tracker(models.Model):

    user_id = models.CharField(verbose_name=u'Users_Email_id',max_length=50, null=True, blank=False)
    device_id = models.CharField(verbose_name=u'Device_id',max_length=50, null=False, blank=False)
    from_screen_id=models.IntegerField(verbose_name=u'Screen_id',max_length=15, null=True, blank=False)
    clicked_on=models.CharField(verbose_name=u'Action',max_length=50, null=True, blank=False)
    datetime=models.DateTimeField(auto_now_add=False, verbose_name='Creation Date')
    imei=models.CharField(verbose_name=u'IMEI',max_length=50, null=True, blank=False)
    price=models.DecimalField(verbose_name=u'Price',max_digits=10, decimal_places=2, null=True, default=0)
    book_mag_id=models.IntegerField(verbose_name=u'Book&Magazine_id',max_length=10, null=True,blank=False, default=0)
    book_type=models.IntegerField(verbose_name=u'Type_of_Book',max_length=2, null=True, choices=settings.BOOKTYPESPICE)
    tag_name=models.CharField(verbose_name=u'Spice_Tag',max_length=25, null=True)
    model_num=models.CharField(verbose_name=u'Device_Model_Num',max_length=25, null=True)
    book_name=models.CharField(verbose_name=u'Book&MagazineName',max_length=50, null=True)
    token=models.CharField(max_length=50,null=True, blank=True,verbose_name='Transaction Token')
    category_name=models.CharField(max_length=50,null=True, blank=True,verbose_name='Category Name')
    download_status=models.CharField(max_length=50,null=True, blank=True,verbose_name='Download Status')
    search_key=models.CharField(max_length=50,null=True, blank=True,verbose_name='Search Name')
    filter=models.CharField(max_length=50,null=True, blank=True,verbose_name='Filter Name')

    class Meta:
        verbose_name_plural = 'View_Tracker'
        verbose_name = 'View_Tracker'
        db_table = 'view_tracker'

    def __unicode__(self):
        return "{}:{}".format(self.user_id, self.device_id)
