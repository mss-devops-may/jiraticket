# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://harishnaidu.atlassian.net/rest/api/3/project"
api_token="ATATT3xFfGF0BbrDOFbQcxghUPLiYzyBoLD5s-XbzvPBFN1LIC8a9bHRdvk6uKKNYEbsS4qQtUwlRWvAv_5LqVfr8USacSjhySlA6rMQo4xpRIn1T6wtAnqvopY4n6wNhw2lfzJv2rvLEOASFYuxR75j9KPVA_gVYPR-Q9EKggnaHkmAbV9fQkQ=3EEEEFAB"

auth = HTTPBasicAuth("rajeshrajaroyal@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]
print (name)
