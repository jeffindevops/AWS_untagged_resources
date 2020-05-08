from config import conf

class ec2_details:
    """
    Main class for boto3 client for ec2
    """
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('ec2')

        self.region_list = []
        # fetching all ec2 regions from describe_regions api call (this is only for ec2)
        self.region_list = [i['RegionName'] for i in self.connection.describe_regions()['Regions']]

    def get_instances(self):
        """
        Getting all instance details for every region
        """

        self.clients = []
        self.clients.append(self.connection)
        self.instances_list = []
        [self.instances_list.append(i.describe_instances()) for i in self.clients]

        return self.instances_list



    def get_volumes(self):
        """
        fetching volume details for running instance
        """
        response = self.connection.describe_volumes()
        return response['Volumes']


    def get_snapshots(self):
        """
        Fetching snapshot details from ec2
        """
        response = self.connection.describe_snapshots()
        return response['Snapshots']

    def get_amis(self):
        """
        Fetching ami details from ec2
        """

        response = self.connection.describe_images()
        return response['Images']

class instance_details:
    """
    Instance details class
    """
    def __init__(self,instance):
        self.instance = instance
        self.tag = ''

        if 'Tags' in self.instance['Instances'][0].keys():
            for t in self.instance['Instances'][0]['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']

        self.id = self.instance['Instances'][0]['InstanceId']



class volume_details:
    """
    Volume details class
    """
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['VolumeId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']


class snapshot_details:
    """
    Snapshot details class
    """
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['SnapshotId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']

class ami_details:
    """
    Ami details class
    """
    def __init__(self,instance):
        self.instance = instance
        self.project = ''
        self.id = self.instance['ImageId']

        if 'Tags' in instance.keys():
            for t in self.instance['Tags']:
                if t['Key'] == conf['tag']:
                    self.tag = t['Value']
