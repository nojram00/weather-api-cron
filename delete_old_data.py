import requests
from cron_constants import URL
from pprint import pprint


fc_response = requests.delete(URL+"forecast-conditions/cleanup-old")
pprint(fc_response.json())

ww_response = requests.delete(URL+"wind-and-coastal-waters/cleanup-old")
pprint(ww_response.json())



