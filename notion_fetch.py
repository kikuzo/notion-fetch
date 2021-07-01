import json
import requests
import datetime

NOTION_HOST="https://api.notion.com"
NOTION_TOKEN="notion access token"
NOTION_DATABASE="notion target database"
NOTION_USERID="notion user id"

PIXELA_GRAPH_URL = "https://pixe.la/v1/users/user-id/graphs/taget-graph"
PIXELA_TOKEN = "pixela token"

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/slackwebhookurl"
SLACK_TARGET_CHANNEL = "target channel"

def fetch_notion():
    headers = {
        'Authorization': 'Bearer ' + NOTION_TOKEN,
        'Notion-Version': '2021-05-13',
        'Content-Type': 'application/json'
    }
    url = NOTION_HOST + "/v1/databases/" + NOTION_DATABASE + "/query"

    utcnow = datetime.datetime.utcnow()
    utcyesterday = utcnow + datetime.timedelta(days=-1)
    utcyesterdaystr = utcyesterday.strftime('%Y-%m-%dT%H:%M:%S') + utcyesterday.strftime('.%f')[:4] + 'Z'
    #print(utcyesterdaystr)

    send_data =  {
        "filter":{
          "and":[
            {
              "property": "Author",
                "created_by": {
                  "contains" : NOTION_USERID
                }
            },
            {
              "property": "Date",
                "date": {
                  "after" : utcyesterdaystr
               }
            }
          ]
        },
        "sorts": [
          {
                "property":"Date",
                #"timestamp": "created_time",
                #"direction": "ascending"
                "direction": "descending"
          }
        ]
    }

    with requests.post(url, data=json.dumps(send_data), headers=headers) as response: 
        response_body = response.json()

    return(response_body)

def pixela_pixelpost_today(count):
    headers = {
      'X-USER-TOKEN' : PIXELA_TOKEN
    }
    send_data = {
      "date": datetime.date.today().strftime('%Y%m%d'),
      "quantity": str(count),
    }
    #print(send_data)

    with requests.post(PIXELA_GRAPH_URL, data=json.dumps(send_data), headers=headers) as response:
      response_body = response.json()
    
def send_message(msg):
    # make slack message body
    send_data = {
        "channel": SLACK_TARGET_CHANNEL,
        "username": "webhook-test-bot",
        "text": msg
    }

    with requests.post(SLACK_WEBHOOK_URL, data=json.dumps(send_data)) as response:
        response_body = response.content

def lambda_handler(event, context):
    # TODO implement
    response = fetch_notion()
    pages = response['results']
    print(pages)
    #send_message(str(len(pages)) + "件のページがありました"))
    #pixela_pixelpost_today(len(pages))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == '__main__':
  response = fetch_notion()
  pages = response['results']
  print(pages)
  #send_message(str(len(pages)) + "件のページがありました"))
  #pixela_pixelpost_today(len(pages))
