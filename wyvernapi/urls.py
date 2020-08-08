from rest_framework.routers import DefaultRouter
from django.urls import path, include

from wyvernapi.views.jobs import WyvernJobsViewSet
from wyvernapi.views.subscribers import WyvernSubscriptionViewSet
from wyvernapi.views.datastore import WyvernDataStoreViewSet


router = DefaultRouter()
router.register("jobs", WyvernJobsViewSet, basename="jobs")
router.register("subscribers", WyvernSubscriptionViewSet, basename="subscribers")
router.register("datastore", WyvernDataStoreViewSet, basename="datastore")

urlpatterns = [
    path("", include(router.urls)),
]
