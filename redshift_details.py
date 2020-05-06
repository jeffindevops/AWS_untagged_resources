class redshift_details:
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('redshift')


    def get_instances(self):

        response = self.connection.describe_clusters()
        return response['Clusters']

class cluster_details:
    def __init__(self,cluster):
        self.cluster = cluster
        self.name = self.cluster['ClusterIdentifier']
        if 'Tags' in self.cluster.keys():
            self.tags = self.cluster['Tags']
            for t in self.tags:
                if 'PROJECT' in t.values():
                    self.project = t['Value']







