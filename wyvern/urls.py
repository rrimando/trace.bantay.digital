"""

Wyvern Core - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from . import views as wyvern_views
from wyvernsite.urls import urlpatterns as wyvernsite_urls
from wyvernblog.urls import urlpatterns as wyvernblog_urls
from wyvernshop.urls import urlpatterns as wyvernshop_urls
from wyvernjobs.urls import urlpatterns as wyvernjobs_urls
from wyvernthemes.urls import urlpatterns as wyvernthemes_urls
from wyvernsearch.urls import urlpatterns as wyvernsearch_urls
from wyvernscraper.urls import urlpatterns as wyvernscraper_urls
from wyverndatastorage.urls import urlpatterns as wyverndatastore_urls
from wyvernsubscriptions.urls import urlpatterns as wyvernsubscriptions_urls

# Client Specific URLS
# from wyvernmetamorph.urls import urlpatterns as wyvernmetamorph_urls

from wyverntrace.urls import urlpatterns as wyverntrace_urls

# API URLS
from wyvernapi.urls import urlpatterns as wyvernapi_urls

# LMS URLS
from wyvernlms.urls import urlpatterns as wyvernlms_urls

# LMS URLS
from wyverncontent.urls import urlpatterns as wyverncontent_urls

import wyvernblog.views as wyvernblog_views
import wyvernshop.views as wyvernshop_views
import wyverncontact.views as wyverncontact_views

urlpatterns = [
    path("", wyvern_views.index, name="core-index"),
    # User Pages
    path("login/", LoginView.as_view(), name="core-login"),
    path("logout/", LogoutView.as_view(), name="core-login"),
    path("account/", wyvern_views.account, name="core-account"),
    path("profile/", wyvern_views.profile, name="core-profile"),
    path("dashboard/", wyvern_views.dashboard, name="core-dashboard"),
    # Django Admin
    # path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # CKEditor
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
    # User Endpoints
    path("signup/", wyvern_views.signup, name="core-signup"),
    # Client Specific URLs
    # path('mtp/', include(wyvernmetamorph_urls)),
    path("trace/", include(wyverntrace_urls)),
]

# Add Static Folder
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Media Folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Error Handling
handler404 = "wyvern.views.handler404"
handler500 = "wyvern.views.handler500"
