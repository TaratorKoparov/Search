import os
import requests
from requests.auth import HTTPBasicAuth

# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir, date_range_filter

PLANET_API_KEY = '19f4c6c1a95c42e498cbeb764da51da9'

# Stats API request object
stats_endpoint_request = {
  "interval": "year",
  "item_types": ["REOrthoTile"],
  "filter": date_range_filter
}

import json

print json.dumps(stats_endpoint_request)

# fire off the POST request
result = \
  requests.post(
    'https://api.planet.com/data/v1/stats',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''),
    json=stats_endpoint_request)

print result.text