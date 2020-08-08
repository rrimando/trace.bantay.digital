""" 

Wyvern Core - URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from . import views as wyvern_views
from wyvernsite.urls import urlpatterns as wyvernsite_urls
from wyvernblog.urls import urlpatterns as wyvernblog_urls
from wyvernshop.urls import urlpatterns as wyvernshop_urls
from wyvernjobs.urls import urlpatterns as wyvernjobs_urls
from wyvernthemes.urls import urlpatterns as wyvernthemes_urls
from wyvernsearch.urls import urlpatterns as wyvernsearch_urls
from wyvernmembers.urls import urlpatterns as wyvernmembers_urls
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
    path("login/", auth_views.login, name="core-login"),
    path("logout/", auth_views.logout, name="core-login"),
    path("account/", wyvern_views.account, name="core-account"),
    path("profile/", wyvern_views.profile, name="core-profile"),
    path("dashboard/", wyvern_views.dashboard, name="core-dashboard"),
    # Django Admin
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("data/", include(wyverndatastore_urls)),
    path("site/", include(wyvernsite_urls)),
    path("blog/", include(wyvernblog_urls)),
    path("shop/", include(wyvernshop_urls)),
    path("jobs/", include(wyvernjobs_urls)),
    path("search/", include(wyvernsearch_urls)),
    path("themes/", include(wyvernthemes_urls)),
    path("members/", include(wyvernmembers_urls)),
    path("scraper/", include(wyvernscraper_urls)),
    path("subscriptions/", include(wyvernsubscriptions_urls)),
    # Custom Content Editor
    path("cc/", include(wyverncontent_urls)),
    # Wyvern API
    path("api/", include(wyvernapi_urls)),
    # Full Application Suites
    # Wyvern LMS
    path("lms/", include(wyvernlms_urls)),
    # Common Pages
    # TODO: About
    # Contact
    path("contact/", wyverncontact_views.index, name="contact-page"),
    path("contact/survey", wyverncontact_views.survey, name="contact-survey"),
    path(
        "contact/form-submission",
        wyverncontact_views.form_submission,
        name="form-submission",
    ),
    # Content Views
    url(r"^page/(?P<slug>[-\w]+)/$", wyvernblog_views.view, name="page-view"),
    url(r"^post/(?P<slug>[-\w]+)/$", wyvernblog_views.view, name="post-view"),
    url(r"^job-post/(?P<slug>[-\w]+)/$", wyvernblog_views.view, name="job-post-view"),
    path("job-posts/", wyvernblog_views.jobs, name="job-post-list"),
    path("news/", wyvernblog_views.list, name="post-list"),
    # Shop Views
    url(r"^catalog/", wyvernshop_views.product_list, name="product-list"),
    url(
        r"^product/(?P<slug>[-\w]+)/$",
        wyvernshop_views.product_view,
        name="product-view",
    ),
    url(
        r"^product-category/(?P<slug>[-\w]+)/$",
        wyvernshop_views.product_category_view,
        name="product-category-view",
    ),
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
