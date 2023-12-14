# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://harishnaidu.atlassian.net/rest/api/3/issue"

api_token="ATATT3xFfGF0BbrDOFbQcxghUPLiYzyBoLD5s-XbzvPBFN1LIC8a9bHRdvk6uKKNYEbsS4qQtUwlRWvAv_5LqVfr8USacSjhySlA6rMQo4xpRIn1T6wtAnqvopY4n6wNhw2lfzJv2rvLEOASFYuxR75j9KPVA_gVYPR-Q9EKggnaHkmAbV9fQkQ=3EEEEFAB"


auth = HTTPBasicAuth("salagundlaharish@gmail.com", api_token )

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First Jira Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10006"
    },
    "project": {
      "key": "HAR"
    },

    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
