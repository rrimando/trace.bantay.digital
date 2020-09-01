"""

Wyvern Contact - Views
    
"""
import re
import urllib
import wyvern.util.config as config

from configparser import ConfigParser, NoOptionError, NoSectionError

from django.urls import reverse
from django.contrib import messages

from django.core import mail
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render

from wyvern.util.chidori import wyvern_core

from django.core.mail import EmailMessage
from django.test.utils import override_settings


def send_with_alt_config(request, subject, message, email_from, recipient_list):

    connection = mail.get_connection(
        host=config.get(request.site.site_url, "email_host"),
        port=config.get(request.site.site_url, "email_port"),
        username=config.get(request.site.site_url, "email_host_user"),
        password=config.get(request.site.site_url, "email_host_password"),
        # ssl = (config.get(request.site.site_url, 'email_use_ssl') == 'True'),
        # tls = (config.get(request.site.site_url, 'email_use_tls')  == 'True')
        # DEFAULT_FROM_EMAIL = config.get(request.site.site_url, 'default_from_email')
    )

    connection.open()

    email = EmailMessage(
        subject,
        message,
        config.get(request.site.site_url, "email_host_user"),
        reply_to=[config.get(request.site.site_url, "email_host_user")],
        to=recipient_list,
        connection=connection,
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.send()

    connection.close()

    return email


@wyvern_core
def index(request):

    if request.method == "POST":
        if email_filter(request):
            messages.add_message(
                request, messages.INFO, "We could not send your message!"
            )

            return redirect(reverse("contact-page"))

        subject = "You have an inquiry from " + request.site.site_name
        message = "From: {}\n".format(request.POST.get("name", ""))
        message += "Company: {}\n".format(request.POST.get("company", ""))
        message += "Address: {}\n".format(request.POST.get("address", ""))
        message += "Email: {}\n".format(request.POST.get("email", ""))
        message += "Telephone: {}\n".format(request.POST.get("telephone", ""))
        message += "Inquiry: {}\n".format(request.POST.get("inquiry", ""))

        if request.POST.get("product", ""):
            message += "Product: {}\n".format(request.POST.get("product", ""))

        email_from = request.site.site_notifications_from
        recipient_list = [
            email.strip()
            for email in request.site.site_notifications_recipients.split(",")
        ]

        try:
            if config.get(request.site.site_url, "email_host"):
                send_with_alt_config(
                    request, subject, message, email_from, recipient_list
                )
        except NoOptionError:
            send_mail(subject, message, email_from, recipient_list)

        messages.add_message(request, messages.INFO, "Your inquiry has been sent!")

        return redirect(reverse("contact-page"))

    else:
        """
        Serve the custom sites
        """
        if request.site:
            site_template = "themes/{}/contact.html".format(request.site.site_template)

            return render(request, site_template, {"page": "contact"})

        else:
            return HttpResponse(
                "Come back in a while as something awesome will here soon!"
            )


@wyvern_core
def survey(request):

    if request.method == "POST":
        if email_filter(request):
            messages.add_message(
                request, messages.INFO, "We could not send your message!"
            )

            return redirect(reverse("contact-page"))

        subject = "You have an inquiry from " + request.site.site_name
        message = "From: {}\n".format(request.POST.get("name", ""))
        message += "Email: {}\n".format(request.POST.get("email", ""))
        message += "Telephone: {}\n\n\n".format(request.POST.get("number", ""))

        if request.POST.get("how_much_do_you_owe", ""):
            message += "How much do you owe?: {}\n".format(
                request.POST.get("how_much_do_you_owe", "")
            )

        if request.POST.get("what_is_your_issue", ""):
            message += "What is your issue?: {}\n".format(
                request.POST.get("what_is_your_issue", "")
            )

        if request.POST.get("state", ""):
            message += "State: {}\n".format(request.POST.get("state", ""))

        email_from = request.site.site_notifications_from
        # recipient_list = ['rohan.rimando@gmail.com','jcbalagot27@gmail.com'] # TODO: Pull from settings
        recipient_list = [
            email.strip()
            for email in request.site.site_notifications_recipients.split(",")
        ]

        try:
            if config.get(request.site.site_url, "email_host"):
                send_with_alt_config(
                    request, subject, message, email_from, recipient_list
                )
        except NoOptionError:
            send_mail(subject, message, email_from, recipient_list)

        # messages.add_message(request, messages.INFO, 'We have received the details of your query. A tax specialist will be in contact with you within a 24 hour time-frame, via Phone call or e-mail with a tax estimate to address your current need')

        return redirect(reverse("page-view", kwargs={"slug": "survey-success"}))

    else:
        """
        Serve the custom sites
        """
        if request.site:
            site_template = "themes/{}/contact.html".format(request.site.site_template)

            return render(request, site_template, {"page": "contact"})

        else:
            return HttpResponse(
                "Come back in a while as something awesome will here soon!"
            )


@wyvern_core
def form_submission(request):

    if request.method == "POST":
        if email_filter(request):
            send_mail(
                "Blocked Email",
                request.site.site_url,
                "system@wyverncms.com",
                ["rohan.rimando@gmail.com"],
            )
            messages.add_message(
                request, messages.INFO, "We could not send your message!"
            )

            return redirect(reverse("contact-page"))

        subject = "A Custom Form Has Been Submitted " + request.site.site_name

        message = ""
        sorted_form_submission = [None] * len(request.POST)

        for key in request.POST:

            if key != "csrfmiddlewaretoken":

                _key = key.split("|")

                sorted_form_submission[int(_key[0])] = _key[1] + "|" + request.POST[key]

        for key in sorted_form_submission:

            if key:
                __values = key.split("|")

                if "html" in __values[0]:
                    message += __values[1]
                else:
                    message += "<strong>{}</strong> : {}<br/>".format(
                        ((" ").join(__values[0].split("_"))).title().strip(),
                        __values[1],
                    )

        email_from = request.site.site_notifications_from
        recipient_list = [
            email.strip()
            for email in request.site.site_notifications_recipients.split(",")
        ]
        # recipient_list += ['rohan.rimando@gmail.com']
        plain_text = strip_tags(re.sub("<br\s*?>", "\n", message))

        try:
            if config.get(request.site.site_url, "email_host"):
                send_with_alt_config(
                    request, subject, message, email_from, recipient_list
                )
        except NoOptionError:
            send_mail(
                subject, message, email_from, recipient_list, html_message=message
            )

        messages.add_message(
            request,
            messages.INFO,
            "We have received the your submission. Please keep your lines open as we will be in touch with you soon! Have a great day!",
        )

        return redirect(reverse("jobs-index"))

    else:
        """
        Serve the custom sites
        """
        if request.site:
            site_template = "themes/{}/contact.html".format(request.site.site_template)

            return render(request, site_template, {"page": "contact"})

        else:
            return HttpResponse(
                "Come back in a while as something awesome will here soon!"
            )


def email_filter(request):

    spam_filters = config.get("filter", "filters").split("\n")

    blocked = False

    for key in request.POST:
        for spam_filter in spam_filters:
            if spam_filter.strip() in request.POST.get(key):
                return True

    return blocked


# EOF
