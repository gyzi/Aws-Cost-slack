# Aws-Cost-slack

## AWS Daily Cost Checker

This is a Python script that retrieves the daily cost for an AWS account and sends a notification to a Slack channel.

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages with `pip install -r requirements.txt`.
3. Create a Slack app and a webhook URL for your Slack channel.
4. Set the environment variables `SLACK_WEBHOOK_URL` and `AWS_PROFILE` with your webhook URL and AWS profile name respectively.

## Usage

To run the script, simply execute the following command in your terminal:
```
python aws-cost.py
```

By default, the script will retrieve the daily cost for the previous day and send it to your Slack channel. You can customize the date range by passing the `--start-date` and `--end-date` arguments in the following format: `YYYY-MM-DD`. For example:

```
python aws-cost.py --start-date 2022-01-01 --end-date 2022-01-31
```


## GitLab CI Pipeline

To run this script daily, you can use GitLab CI/CD scheduled pipelines. Here is an example `.gitlab-ci.yml` file:

Gitlab variables to be set:
  AWS_DEFAULT_REGION: "us-east-1"
  SLACK_WEBHOOK_URL: https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX

```yaml
stages:
  - daily_aws_cost

daily_cost:
  stage: daily_aws_cost
  image: python:3.9
  script:
    - pip3 install -r requirements.txt
    - python3 aws-cost.py
  only:
    - schedules
```
This pipeline will run the script daily at midnight UTC.
