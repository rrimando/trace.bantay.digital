"""
    Wyvern Jobs Context 
"""
from .models import WyvernJobs


# This might not be the best way to display custom posts
def jobs(request):

    try:
        request.site
    except AttributeError:
        jobs = None
    else:
        jobs = WyvernJobs.objects.filter(job_site=request.site).all()

    return {"jobs": jobs}
