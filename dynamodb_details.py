from config import conf

class dynamodb_details:
    """
    Main class for boto3 client for DynamoDB
    """
    def __init__(self,session_client):
        self.session = session_client
        self.connection = self.session.client('dynamodb')


    def get_instances(self):
        """
        Getting all instance
        """

        response = self.connection.list_tables()
        return response['TableNames']

    def get_arn(self,table):
        """
        Getting table arn for given table
        """
        res = self.connection.describe_table(TableName=table)
        return res['Table']['TableArn']

    def get_tags(self,arn):
        """
        Fetching tags for table
        """
        response = self.connection.list_tags_of_resource(ResourceArn=arn)
        if 'Tags' in response.keys():
            return response['Tags']
        else:
            return []



class table_details:
    """
    Table details class
    """
    def __init__(self,table):
        self.table = table

    def assign_tags(self,tag):
        self.tag = ''

        for t in tag:
            if conf['tag'] in t.values():
                self.tag = t['Value']
