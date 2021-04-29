import requests
url = 'https://autoportal.com/mahindra/car-dealers/bangalore/page/3'

if requests.get(url).status_code == 404:
    print("NA")
