from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# Creating a flask app instance
app = Flask(__name__)

@app.route("/createJIRA" , methods=['POST'])
def createJIRA():
        
    
    url = "https://harishnaidu.atlassian.net/rest/api/3/issue"

    api_token="ATATT3xFfGF0BbrDOFbQcxghUPLiYzyBoLD5s-XbzvPBFN1LIC8a9bHRdvk6uKKNYEbsS4qQtUwlRWvAv_5LqVfr8USacSjhySlA6rMQo4xpRIn1T6wtAnqvopY4n6wNhw2lfzJv2rvLEOASFYuxR75j9KPVA_gVYPR-Q9EKggnaHkmAbV9fQkQ=3EEEEFAB"


    auth = HTTPBasicAuth("rajeshrajaroyal@gmail.com", api_token )

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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    

app.run('0.0.0.0', port=5000)

