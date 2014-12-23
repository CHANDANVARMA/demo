from django.http import HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest, HttpResponse

from django.utils.decorators import available_attrs
from django.utils.log import getLogger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from functools import wraps


logger = getLogger('django.request')

"""
    Decorator to make a view only accept particular request methods.  Usage::

        @check_http_paramters("GET", ["uname","passwd"])
    Note that request methods should be in uppercase.
"""
def check_http_paramters(request_method, param_list):
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):

            # check if this is acceptable request type
            if request.method != request_method:
                logger.warning('Method Not Allowed (%s): %s', request.method, request.path,
                    extra={
                        'status_code': 405,
                        'request': request
                    }
                )
                return HttpResponseNotAllowed(request_method)

            paramters = {}
            rmethod = getattr(request, request.method)

            # fill all parameters
            for key, val in rmethod.iteritems():
                paramters[key] = val

            #check paramters...
            for param in param_list:
                if paramters.get(param, None) is None:

                    if settings.DEBUG_PARAMTER_NOT_FOUND:
                        from reqresp import errorInsufficientParamters
                        return errorInsufficientParamters(param)
                    else:
                        return HttpResponseBadRequest()

            kwargs['paramters'] = paramters
            return func(request, *args, **kwargs)
        return inner
    return decorator


def is_operator_network(f):
    def wrap(request, *args, **kwargs):

        if not request.httpclientinfo.get('is_operator', False):
            return HttpResponse("""{"errorcode": 8001, "errorstring": "Please use mobile network", "success": false}""", status=412, mimetype="application/json")

        if len(request.httpclientinfo.get('msisdn', '')) <= 0:
            return HttpResponse("""{"errorcode": 8002, "errorstring": "Invalid MSISDN", "success": false}""", status=412, mimetype="application/json")

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


#decorater to not to allow non-supplier user.
def publisher_login_required(f):
    def wrap(request, *args, **kwargs):

        from publishers.views import check_if_user_is_publisher
        if not check_if_user_is_publisher(request.user):
            messages.error(request, "Only publishers are allowed to login!")
            return HttpResponseRedirect("/publishers/logout/")
        func = login_required(f)
        return func(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def check_hash(f):
    def wrap(request, *args, **kwargs):
        params = kwargs.get('paramters')
        signature = params.get('signature', None)
        if signature and signature is not None:
            del params[settings.SIGNATURE]
            response = check_signature(request, params)
            if response.get('success', None):
                hashmap = response.get('hash', None)
                if str(hashmap) != str(signature):
                    return HttpResponse(status='412')
            else:
                return HttpResponse(status='412')
        else:
            return HttpResponse(status='412')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
