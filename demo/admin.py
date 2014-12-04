from django.contrib import admin
from models import Spice_Login


class Spice_LoginAdmin(admin.ModelAdmin):

    list_display=('spice_user_name','spice_user_password')
    list_filter=('spice_user_name',)
    list_per_page=15

admin.site.register(Spice_Login, Spice_LoginAdmin)