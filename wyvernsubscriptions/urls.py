from django.urls import path

from wyvernsubscriptions import views

urlpatterns = [
    path("", views.WyvernSubscribersList.as_view(), name="sub_list"),
    path("view/<int:pk>", views.WyvernSubscribersView.as_view(), name="sub_view"),
    path("new", views.WyvernSubscribersCreate.as_view(), name="sub_new"),
    path("view/<int:pk>", views.WyvernSubscribersView.as_view(), name="sub_view"),
    path("edit/<int:pk>", views.WyvernSubscribersUpdate.as_view(), name="sub_edit"),
    path("delete/<int:pk>", views.WyvernSubscribersDelete.as_view(), name="sub_delete"),
    path("export", views.export, name="sub_export"),
]
