from config import conf

class redshift_details:
    """
    Main class for boto3 client for redshift
    """
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('redshift')


    def get_instances(self):

        response = self.connection.describe_clusters()
        return response['Clusters']

class cluster_details:
    """
    Redshift cluster details class
    """
    def __init__(self,cluster):
        self.cluster = cluster
        self.name = self.cluster['ClusterIdentifier']
        self.tag = ''
        if 'Tags' in self.cluster.keys():
            self.tags = self.cluster['Tags']
            for t in self.tags:
                if conf['tag'] in t.values():
                    self.tag = t['Value']
