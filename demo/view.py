from django.contrib.auth.views import logout as core_logout
from models import Spice_Login,View_Tracker
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from decorator import check_http_paramters
from django.conf import settings
from error import ERROR_DICT
from django.http import HttpResponse
from django.views.generic import View
import json

def login(request):
    #import pdb;pdb.set_trace()
    template_name="EventTracker/short_code.html"
    context={}
    if request.method=="POST":
        username=request.POST['UserName']
        password=request.POST['Password']
        user = Spice_Login.objects.filter(spice_user_name=username, spice_user_password=password)
        if user.count():
            request.session['is_logged_in'] = True
            request.session['username'] = username
            return redirect('/spice/')
        else:
            message="You are not authorized"
            context={'message':message}
            return render(request,template_name,context)
    if request.session.get('username'):
        return redirect('/spice')
    return render(request,template_name,context)


def logout(request, next_page='/login/'):
    request.session.flush()
    return core_logout(request, next_page)


def spice(request):
    user = request.session.get("username", "")
    if not user:
        return redirect("/login")
    template_name="EventTracker/interface.html"
    message="most welcome"
    context={'message':message}
    return render(request,template_name,context)

def view_tracker(request):
    user_id=request.GET['user_id']
    device_id=request.GET['device_id']
    from_screen_id=request.GET['from_screen_id']
    clicked_on=request.GET['clicked_on']
    datetime=request.GET['datetime']
    imei=request.GET['imei']
    price=request.GET['price']
    book_mag_id=request.GET['book_mag_id']
    book_type=request.GET['book_type']
    tag_name=request.GET['tag_name']
    model_num=request.GET['model_num']
    book_name=request.GET['book_name']
    token=request.GET['token']
    category_name=request.GET['category_name']
    download_status=request.GET['download_status']
    search_key=request.GET['search_key']
    filter=request.GET['filter']


    view_tracker = View_Tracker()
    view_tracker.user_id = user_id
    view_tracker.device_id = device_id
    view_tracker.from_screen_id = from_screen_id
    view_tracker.clicked_on = clicked_on
    view_tracker.datetime = datetime
    view_tracker.imei=imei
    view_tracker.price=price
    view_tracker.book_mag_id=book_mag_id
    view_tracker.book_type=book_type
    view_tracker.tag_name=tag_name
    view_tracker.model_num=model_num
    view_tracker.book_name=book_name
    view_tracker.token=token
    view_tracker.category_name=category_name
    view_tracker.download_status=download_status
    view_tracker.search_key=search_key
    view_tracker.filter=filter

    view_tracker.save()
    scm1 = View_Tracker.objects.all().order_by('-id')[0].id
    return JsonResponse ({'id': scm1, })

'''def time(value, arg=None):
    "Formats a time according to the given format"
    from django.utils.dateformat import time_format
    if not value:  ## BUG!
        return ''  ##
    if arg is None:
        arg = settings.TIME_FORMAT
    return time_format(value, arg)'''


'''@csrf_exempt
@check_http_paramters("GET", ['spice_user_name','spice_user_password',])
def GetSearchAndroid(request, paramters=None):

    output = {}
    start = paramters.get('start', 0)
    count = paramters.get('count', 10)
    spice_user_name = paramters.get('spice_user_name','')
    spice_user_password = paramters.get('spice_user_password','')
    query = paramters.get('query', '')
    query = query.strip()
    if query :
        Spice_Login.objects.create(searchkey=query, fullpath=request.get_full_path())

    search_result = []


    # check if indices are valid ...
    indices_resp, start, count = _indices_check(start, count)
    if indices_resp is False:
        return returnErrorShorcut(500420, ERROR_DICT[500420])

    if settings.USE_SEARCH_ENGINE:
        search_result = ContentSearch().get_newui_results(searchquery=query, start=start, count=count, spice_user_name=spice_user_name,spice_user_password=spice_user_password)

        if len(search_result) <= 0:
            return returnErrorShorcut(500212, ERROR_DICT[500212])

    output['bookslist'] = search_result

    return returnSuccessShorcut(output)

def returnErrorShorcut(error_code, error_Status, httpstatus=200):
    output = {}
    output['success'] = False
    output['errorcode'] = error_code
    output['errorstring'] = error_Status
    return returnresponsejson(output, httpstatus)


def returnSuccessShorcut(param_dict={}, httpstatus=200):
    param_dict['success'] = True
    return returnresponsejson(param_dict, httpstatus)


def returnresponsejson(pass_dict, httpstatus=200):
    json_out = JsonResponse.dumps(pass_dict)
    return HttpResponse(json_out, status=httpstatus, mimetype="application/json")


def _indices_check(start, count):
    try:
        start = int(start)
        count = int(count)
        if start < 0 or count < 1 or count > 20:
            return False, '', ''
    except ValueError:
        return False, '', ''

    return True, start, count


class ContentSearch(View, JsonResponse):

    def get_newui_results(self,searchquery=None, start=0, count=10, booktype=1, **kwargs):
        output={}
    return output '''






