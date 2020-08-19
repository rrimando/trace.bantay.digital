import urllib
import datefinder
import bs4

from datetime import datetime
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as request  # Web client

now = datetime.now()


class Scraper:
    def __init__(self, config):
        print("CONFIGURING SCRAPER")

        self.counter = 1

        # File modification

        self.config = config["config"]

    def start(self):

        print("STARTING SCRIPT")

        parsed_data = {}

        for configuration in self.config:
            print("(" + str(self.counter) + ")FETCHING : " + configuration["url"])

            config_targets = configuration["targets"]

            try:
                client = request(configuration["url"])

            except urllib.error.HTTPError as e:
                if e.code == 404 or e.code == 403:

                    print("PAGE DOES NOT EXIST!")
                    continue
            else:
                pagecontent = client.read()
                client.close()

                # Parse Data
                for data_target in config_targets:

                    # Grab Data
                    if data_target["container"]:
                        parsed_data[data_target["container"]] = (
                            self.parse(
                                pagecontent,
                                data_target["element"],
                                data_target["target"],
                            )
                        ).decode("utf-8")

                    else:
                        print("PAGE COULD NOT BE REACHED OR WAS REDIRECTED")

                    self.counter += 1

        print("ENDED SCRIPT RUN")

        return parsed_data

    def getFileContents(self, fileTarget):
        urls = []

        for line in open(fileTarget, "r"):
            urls.append(line.strip())

        return urls

    def parseHTML(self, html, element, target, html_format=False):
        try:
            result = (
                html.find(element, target).prettify().encode("utf8")
                if html_format
                else html.find(element, target).getText().encode("utf8")
            )

            return result if result and result is not None else ""

        except:
            return ""

    def parse(self, html, element, target):

        html_soup = soup(html, "html.parser")
        target_content = self.parseHTML(html_soup, element, target)
        # variable = self.parseHTML(html_soup, 'div', {"class": "article-content"}, True)
        return target_content
