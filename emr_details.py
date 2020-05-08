from config import conf

class emr_details:
    """
    Main class for boto3 client for emr
    """
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('emr')


    def get_instances(self):
        """
        Fetching all instances
        """

        response = self.connection.list_clusters()
        return response['Clusters']

    def get_tags(self,id):
        """
        Fetching tags from each given cluster id
        """
        response = self.connection.describe_cluster(ClusterId=id)
        if 'Tags' in response['Cluster'].keys():
            return response['Cluster']['Tags']
        else:
            return []



class emr_cluster_details:
    """
    Emr details class
    """
    def __init__(self,cluster):
        self.cluster = cluster
        self.id = self.cluster['Id']
        self.name = self.cluster['Name']
        self.tag = ''

    def assign_tags(self,tag):
        """
        Assign tags for cluster details
        """
        for t in tag:
            if conf['tag'] in t.values():
                self.tag = t['Value']
