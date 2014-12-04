from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.context_processors import csrf
import django.middleware.csrf as csrfmiddleware
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as core_login
from django.contrib.auth.views import logout as core_logout
from models import Spice_Login








def login(request):
    #import pdb;pdb.set_trace()
    template_name="/demo/EventTracker/short_code.html"
    context={}
    if request.method=="POST":
        username=request.POST['UserName']
        password=request.POST['Password']
        user = Spice_Login.objects.filter(spice_user_name=username, spice_user_password=password)
        if user.count():
            request.session['is_logged_in'] = True
            request.session['username'] = username
            return redirect('/Spice/')
        else:
            message="You are not authorized"
            context={'message':message}
            return render(request,template_name,context)
    if request.session.get('username'):
        return redirect("/EventTracker/Spice")
    return render(request,template_name,context)


def logout(request, next_page='/Login/'):
    #messages.success(request, "You have been successfully logged out!")
    request.session.flush()
    return core_logout(request, next_page)


