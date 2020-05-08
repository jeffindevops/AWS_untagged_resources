
from config import conf
region_list = ['us-east-1','us-east-2','us-west-1','us-west-2','ap-south-1','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-northeast-1','ca-central-1','eu-central-1','eu-west-1','eu-west-2','sa-east-1']

class rds_details:
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('rds')


    def get_instances(self):


        ## multi region
        self.clients = []
        for r in region_list:
            tmp_cli = self.session.client('rds',region_name=r)
            self.clients.append(tmp_cli)

        self.instances_list = []
        [self.instances_list.append(i.describe_db_instances()) for i in self.clients]

        # return self.connection.describe_stacks()
        self.connection = self.session.client('rds')
        return self.instances_list

        # return self.connection.describe_db_instances()

    def get_tags(self,cu_arn):
        tags = self.connection.list_tags_for_resource(ResourceName=cu_arn)
        return tags['TagList']



class rds_instance_details:
    def __init__(self,instance):
        self.instance = instance

        ## instance variables
        self.arn = self.instance['DBInstanceArn']
        self.name = self.instance['DBInstanceIdentifier']

    def assign_tags(self,tag):
        self.tag = ''

        for t in tag:
            if t['Key'] == conf['tag']:
                self.tag = t['Value']
