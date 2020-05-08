from config import conf

class ec2_details:
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('ec2')

        self.region_list = []
        self.region_list = [i['RegionName'] for i in self.connection.describe_regions()['Regions']]

        # self.instances = self.get_instances()


    def get_instances(self):


        self.clients = []
        self.clients.append(self.connection)
        self.instances_list = []
        [self.instances_list.append(i.describe_instances()) for i in self.clients]

        return self.instances_list



    def get_volumes(self):
        response = self.connection.describe_volumes()
        return response['Volumes']


    def get_snapshots(self):
        response = self.connection.describe_snapshots()
        return response['Snapshots']

    def get_amis(self):

        response = self.connection.describe_images()
        return response['Images']

class instance_details:
    def __init__(self,instance):
        self.instance = instance
        self.tag = ''

        if 'Tags' in self.instance['Instances'][0].keys():
            for t in self.instance['Instances'][0]['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']

        self.id = self.instance['Instances'][0]['InstanceId']



class volume_details:
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['VolumeId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']


class snapshot_details:
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['SnapshotId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']

class ami_details:
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['ImageId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']
