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
