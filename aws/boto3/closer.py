import os
import boto3
import json


def load_file():

    credfile="creds.json"
    cf = open(credfile , 'r')
    creds = json.load(cf)
    return creds

def read_my_credentials():
    credfile="creds.json"
    cf = open(credfile , 'r')
    creds = json.load(cf)
    client = boto3.client('ec2', aws_access_key_id=creds['access_key_id'],
                                      aws_secret_access_key=creds['secret_access_key'])
    return client
#------------ stop instances ---------------------
def stop_instance(instance_id, reg_name):
    ec2_client = boto3.client("ec2", region_name=reg_name)
    response = ec2_client.stop_instances(InstanceIds=instance_id)
#------------ terminate instances ---------------------
def terminate_instances(instance_id, reg_name):
    ec2_client = boto3.client("ec2", region_name=reg_name)
    response = ec2_client.terminate_instances(InstanceIds=instance_id)
#-----------  delete internet gateways -------------------
def delete_internet_gateways(instance_id, reg_name):
    ec2_client = boto3.client("ec2", region_name=reg_name)
    response =  ec2_client.delete_internet_gateway(InternetGatewayId=instance_id)
#-----------  delete VPCS -------------------
def delete_vpcs(instance_id, reg_name):
    ec2_client = boto3.client("ec2", region_name=reg_name)
    response = ec2_client.delete_vpc(VpcId=instance_id)

def Region_Name():
    client = read_my_credentials()
    all_regions=client.describe_regions()
    list_of_Region=[]
    for each_reg in all_regions['Regions']:
        list_of_Region.append(each_reg['RegionName'])
    creds=load_file()

    for each_reg in list_of_Region:
        session = boto3.Session(aws_access_key_id=creds['access_key_id'],
                                aws_secret_access_key=creds['secret_access_key'],
                                region_name=each_reg)
        resource=session.resource(service_name="ec2") 
        print("List of EC2 instances from the region: " ,each_reg)
        
        for each_in in resource.instances.all():
            print(each_in.id,each_in.state['Name'])
            terminate_instances(each_in.id, each_reg)

        for each_in in resource.internet_gateways.all():
            print(each_in.id)
            delete_internet_gateways(each_in.id, each_reg)

        for vpcid in resource.vpcs.all():
              print(vpcid.id)
              delete_vpcs(vpcid.id, each_reg)


Region_Name()
