import boto3
import json

def CreateNewTopic():

    client = boto3.client("sns")
    topicname= "sns-demo"
    topicArn = 'arn:aws:sns:us-east-1:673714956759:'+topicname
    response = client.create_topic(
            Name=topicname)
    response = client.subscribe(TopicArn=topicArn,
                                Protocol='email',
                                Endpoint='ali.hadish@gmail.com',
                                ReturnSubscriptionArn=True
                                )
    print(response['ResponseMetadata']['HTTPStatusCode'])

    response = client.subscribe(TopicArn=topicArn,
                                Protocol='sms',
                                Endpoint='+972506234979',
                                ReturnSubscriptionArn=True
                                )  
    print(response['ResponseMetadata']['HTTPStatusCode'])

    response = client.subscribe(TopicArn=topicArn,
                                Protocol='lambda',
                                Endpoint='arn:aws:lambda:us-east-1:673714956759:function:DemoSNS',
                                ReturnSubscriptionArn=True
                                )  
    print(response['ResponseMetadata']['HTTPStatusCode'])
CreateNewTopic()

