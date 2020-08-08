"""

Wyvern Scraper - Views
    
"""
import json
import urllib
from django.urls import reverse
import wyvern.util.config as config

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from wyvern.util.chidori import wyvern_core

from wyvernsite.models import WyvernSite
from wyvernblog.models import WyvernPost
from wyvernshop.models import WyvernProduct

from wyvernscraper.wyvernscraper import Scraper


@wyvern_core
def index(request):

    scraper = Scraper(
        {
            "config": [
                {
                    "url": "https://countrymeters.info/en/World",
                    "targets": [
                        {
                            "container": "world_population",
                            "element": "div",
                            "target": {"id": "cp1"},
                        }
                    ],
                },
                # {
                #     'url': 'https://www.buybitcoinworldwide.com/how-many-bitcoins-are-there/',
                #     'targets': [
                #         {
                #             'container': 'bitcoins_left',
                #             'element': 'span',
                #             'target': {"id": "bitcoinsleft"},
                #         },
                #         {
                #             'container': 'bitcoins_issued',
                #             'element': 'span',
                #             'target': {"id": "bitcoinsissued"},
                #         },
                #         {
                #             'container': 'bitcoins_per_day',
                #             'element': 'span',
                #             'target': {"id": "btcperday"},
                #         },
                #         {
                #             'container': 'bitcoins_total',
                #             'element': 'span',
                #             'target': {"id": "totalbtc"},
                #         }
                #     ]
                # },
            ]
        }
    )

    data = scraper.start()

    return JsonResponse(data)
