import boto3
import os
import requests
from datetime import datetime, timedelta
import pytz


AWS_REGION = os.getenv("AWS_REGION")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

end_utc = datetime.utcnow()
start_utc = end_utc - timedelta(days=1)

# Convert UTC to IST
ist = pytz.timezone('Asia/Dubai')
end = end_utc.replace(tzinfo=pytz.utc).astimezone(ist)
start = start_utc.replace(tzinfo=pytz.utc).astimezone(ist)


def get_cost():
    client = boto3.client('ce', region_name=AWS_REGION)
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    return response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']


def send_slack_notification(cost):
    message = f"Daily AWS cost for the last 24 hours is: $ {cost}"
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("Slack notification sent successfully!")
    else:
        print("Error sending Slack notification!")


def main():
    cost = get_cost()
    print(f"Daily cost: $ {cost}")
    send_slack_notification(cost)


if __name__ == "__main__":
    main()
  
