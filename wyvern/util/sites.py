from wyvernsite.models import WyvernSite


def fetch_sites(request):

    if request.user.is_superuser:
        user_sites = WyvernSite.objects.all()
    else:
        user_sites = WyvernSite.objects.filter(site_owner_id=request.user.id)

    return user_sites


def get_site(request):

    return request.META["HTTP_HOST"]
