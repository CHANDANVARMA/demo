from django.contrib import admin
from models import Spice_Login,View_Tracker


class Spice_LoginAdmin(admin.ModelAdmin):

    list_display=('spice_user_name','spice_user_password')
    list_filter=('spice_user_name',)
    list_per_page=15

class View_TrackerAdmin(admin.ModelAdmin):
    list_display = ('user_id','device_id','from_screen_id','datetime','imei','model_num','book_type','price','book_mag_id','tag_name','book_name','clicked_on','token','category_name','download_status','search_key','filter')
    list_filter = ("datetime",)
    list_per_page = 2000

admin.site.register(Spice_Login, Spice_LoginAdmin)
admin.site.register(View_Tracker, View_TrackerAdmin)