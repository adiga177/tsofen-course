import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FirstDy')
############## Create Dynamodb ################
def CreateDy():
    try:
        dynamodb.create_table(
            TableName='FirstDy',
            AttributeDefinitions=[
                {
                    "AttributeName": "partition",
                    "AttributeType": "S"
                }
            ],
            KeySchema=[
                {
                    "AttributeName": "partition",
                    "KeyType": "HASH"
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
            )
        print("Table created successfully.")
    except Exception as e:
        print("Could not create table. Error:")
        print(e)
############## ADD Item to table ################
def AddItemDy(ItemToAdd):
    try:
        response = table.put_item(
            Item={
                'partition': ItemToAdd
                }
                                )   
        print("Item created successfully.")
    except Exception as e:
        print("Could not add Item. Error:")
        print(e)    
############## Delete Item to table ################ 
def DeleteItemDy(ItemToDelete):
    try:
        table.delete_item(
        Key={
            'partition': ItemToDelete 
             }
                        )
        print("Item deleted successfully.")
    except Exception as e:
        print("Could not deleted Item. Error:")
        print(e) 



CreateDy()
AddItemDy("circassia")
AddItemDy("usa")
AddItemDy("israel")
DeleteItemDy("usa")
