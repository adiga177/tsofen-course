import boto3
import json

def main():
    
    topicArn = 'arn:aws:sns:us-east-1:673714956759:sns-demo'
    client = boto3.client("sns")
    publishObject = "My first publish using SNS"
    response = client.publish(TopicArn=topicArn,
                                    Message=publishObject ,
                                    Subject='My First publish ',
                                    MessageAttributes = {"TransactionType": { "DataType": "String", "StringValue": "First publish"}})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Topic send")

    response = client.publish(TopicArn=topicArn,
                                    Message=publishObject ,
                                    Subject='My second publish ',
                                    MessageAttributes = {"TransactionType": { "DataType": "String", "StringValue": "First publish"}})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Topic send")

    response = client.publish(TopicArn=topicArn,
                                    Message=publishObject ,
                                    Subject='My therd publish ',
                                    MessageAttributes = {"TransactionType": { "DataType": "String", "StringValue": "First publish"}})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Topic send")

    response = client.publish(TopicArn=topicArn,
                                    Message=publishObject ,
                                    Subject='My fourth publish ',
                                    MessageAttributes = {"TransactionType": { "DataType": "String", "StringValue": "First publish"}})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Topic send")     
           
main()
