""" 
    URL Utility Helper
  
    Helper for URL and Redirects 

"""
import urllib

from django.http import HttpResponseRedirect

from django.urls import reverse


def custom_redirect(url_name, *args, **kwargs):
    if args:
        url = reverse(url_name)

    else:
        url = reverse(url_name, args=args)

    params = urllib.parse.urlencode(kwargs)

    return HttpResponseRedirect(url + "?%s" % params)
