
# region_list = ['ap-south-1', 'eu-west-2', 'eu-west-1', 'ap-northeast-2', 'ap-northeast-1', 'sa-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
region_list = ['us-east-1']
class opswork_details:
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('opsworks',region_name=region_list[0])


    def get_instances(self):

        self.clients = []

        for r in region_list:
            tmp_cli = self.session.client('opsworks',region_name=r)
            self.clients.append(tmp_cli)

        self.instances_list = []
        [self.instances_list.append(i.describe_stacks()) for i in self.clients]

        # return self.connection.describe_stacks()
        return self.instances_list


    def get_tags(self,cu_arn):

        # try:
        #     tags = self.connection.list_tags(ResourceArn=cu_arn)
        #     return tags['Tags']
        # except:
        #     return {}
        tags = self.connection.list_tags(ResourceArn=cu_arn)
        return tags['Tags']



class opswork_instance_details:
    def __init__(self,instance):
        self.instance = instance

        ## instance variables
        self.arn = self.instance['Arn']
        self.name = self.instance['Name']

    def assign_tags(self,tag):
        self.project = ''

        if 'PROJECT' in tag.keys():
            self.project = tag['PROJECT']
