"""
    Wyvern Blog Context 
"""
from .models import WyvernPost


def pages(request):

    try:
        request.site
    except AttributeError:
        pages = None
    else:
        pages = WyvernPost.objects.filter(
            post_site=request.site, post_type="page"
        ).all()

    return {"pages": pages}


def posts(request):

    try:
        request.site
    except AttributeError:
        posts = None
    else:
        posts = WyvernPost.objects.filter(
            post_site=request.site, post_type="post"
        ).all()

    return {"posts": posts}


# This might not be the best way to display custom posts
def job_posts(request):

    try:
        request.site
    except AttributeError:
        posts = None
    else:
        posts = WyvernPost.objects.filter(post_site=request.site, post_type="job").all()

    return {"job_posts": posts}
