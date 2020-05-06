
class dynamodb_details:
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('dynamodb')


    def get_instances(self):

        response = self.connection.list_tables()
        return response['TableNames']

    def get_arn(self,table):
        res = self.connection.describe_table(TableName=table)
        return res['Table']['TableArn']

    def get_tags(self,arn):
        response = self.connection.list_tags_of_resource(ResourceArn=arn)
        if 'Tags' in response.keys():
            return response['Tags']
        else:
            return []



class table_details:
    def __init__(self,table):
        self.table = table

    def assign_tags(self,tag):
        self.project = ''

        for t in tag:
            if 'PROJECT' in t.values():
                self.project = t['Value']
