"""
    Wyvern LMS Context 
"""
from .models import WyvernLMSStudent


# This might not be the best way to display custom posts
def students(request):

    try:
        request.site
    except AttributeError:
        students = None
    else:
        students = WyvernLMSStudent.objects.filter(
            wyvernlms_wyvern_site=request.site
        ).all()

    return {"students": students}
