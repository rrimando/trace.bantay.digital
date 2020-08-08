import json
import requests

# */10 * * * * /usr/bin/python3 /var/www/wyvern/wyvernscripts/trace.py >> ~/cron.log 2>&1

datastore = {"cases": 0, "age_cases": 0, "others": 0, "details": 0}


def requests_get(url, *args, **kwargs):
    response = requests.get(url, *args, **kwargs)
    return response.content.decode("utf-8")


def parse_json(data):
    return json.loads(data)


def fetch_data():

    datastore["cases"] = requests_get("http://122.55.59.12/covid/api/cases")
    datastore["age_cases"] = requests_get(
        "http://122.55.59.12/covid/api/gender/age/cases"
    )
    datastore["others"] = requests_get("http://122.55.59.12/covid/api/others")
    datastore["details"] = requests_get("http://122.55.59.12/covid/api/case/details")


def store_data(url):
    data = {
        "data_store_identity": "covidstats",
        "data_store_content": json.dumps(datastore),
        "data_store_tags": "Trace, Covid, Bantay Digital",
        "data_store_site": 2,
    }

    post_data = requests.post(url, data)

    print(post_data.content)


fetch_data()
store_data("https://trace.bantay.digital/api/datastore/")

print(datastore)
