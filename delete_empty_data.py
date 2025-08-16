import requests
from cron_constants import URL
from pprint import pprint


fc_response = requests.delete(URL+"forecast-conditions/cleanup-empty")
pprint(fc_response.json())

ww_response = requests.delete(URL+"wind-and-coastal-waters/cleanup-empty")
pprint(ww_response.json())



