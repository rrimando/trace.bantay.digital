import json
import requests

datastore = {
    "total_population": 0,
    "bitcoins_per_person": 0,
    "height": 0,
    "total_number": 0,
    "total_number_fixed": 0,
    "total_bitcoins_issued": 0,
    "total_percent": 0,
    "bitcoins_remaining": 0,
    "formatted_remaining": 0,
    "bitcoins_per_person_formatted": 0,
    "bitcoins_per_person_dollar": 0,
    "price": 0,
}


def requests_get(url, *args, **kwargs):
    response = requests.get(url, *args, **kwargs)
    return response.content.decode("utf-8")


def parse_json(data):
    return json.loads(data)


def calculate_btc():

    pop_request = requests_get("https://btcperperson.com/scraper/")
    pop_data = parse_json(pop_request)

    datastore["total_population"] = pop_data["world_population"]

    latest_block_request = requests_get("https://www.satochi.co/latest-block")

    datastore["height"] = int(latest_block_request)

    datastore["total_number"] = 12.5 * (datastore["height"] - 472500) + 16406250
    datastore["total_number_fixed"] = str(datastore["total_number"]).replace(
        r"/\B(?=(\d{3})+(?!\d))/g", ","
    )
    datastore["total_bitcoins_issued"] = datastore["total_number"] / 21000000 * 100
    datastore["total_percent"] = ("%.2f" % datastore["total_bitcoins_issued"]) + "%"

    latest_request = requests_get("https://www.satochi.co/latest")
    latest_data = parse_json(latest_request)

    datastore["price"] = int(latest_data["Price"])

    datastore["bitcoins_remaining"] = 21000000 - datastore["total_number"]
    datastore["formatted_remaining"] = "{:,}".format(datastore["bitcoins_remaining"])
    datastore["bitcoins_per_person"] = int(datastore["total_number"]) / int(
        datastore["total_population"].replace(",", "")
    )
    datastore["bitcoins_per_person_formatted"] = "{:,}".format(
        datastore["bitcoins_per_person"]
    )
    # datastore['bitcoins_per_person_dollar']  = '$' + str("%.2f" % (datastore['bitcoins_per_person'] * datastore['price']))
    datastore["bitcoins_per_person_dollar"] = "$" + str(
        "%.2f"
        % (
            (
                datastore["total_number"]
                / int(datastore["total_population"].replace(",", ""))
            )
            * datastore["price"]
        )
    ).replace(r"/\B(?=(\d{3})+(?!\d))/g", ",")


def store_data(url):
    data = {
        "data_store_identity": "btcperperson",
        "data_store_content": json.dumps(datastore),
        "data_store_tags": "BTC, BTCperperson",
        "data_store_site": 15,
    }

    post_data = requests.post(url, data)

    print(post_data.content)


calculate_btc()
store_data("https://btcperperson.com/api/datastore/")

print(datastore)
