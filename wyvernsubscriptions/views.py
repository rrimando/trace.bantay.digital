import csv

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from wyvern.util.chidori import wyvern_core

from wyvernsubscriptions.models import WyvernSubscribers


# TODO, Apply chidori and load sites and messages(future proof) for sidebar


class WyvernSubscribersList(ListView):
    model = WyvernSubscribers


class WyvernSubscribersView(DetailView):
    model = WyvernSubscribers


class WyvernSubscribersCreate(CreateView):
    model = WyvernSubscribers
    fields = ["sub_fullname", "sub_email"]
    success_url = reverse_lazy("sub_list")


class WyvernSubscribersUpdate(UpdateView):
    model = WyvernSubscribers
    fields = ["sub_fullname", "sub_email"]
    success_url = reverse_lazy("sub_list")


class WyvernSubscribersDelete(DeleteView):
    model = WyvernSubscribers
    success_url = reverse_lazy("sub_list")


@wyvern_core
def export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="subscriptions.csv"'

    site_subscriptions = WyvernSubscribers.objects.filter(sub_site=request.site).all()

    writer = csv.writer(response)

    for subscriber in site_subscriptions:

        writer.writerow([subscriber.sub_fullname, subscriber.sub_email])

    return response
