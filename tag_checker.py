from sys import exit

from aws_session import aws_session
from ec2_details import ec2_details,instance_details,volume_details,snapshot_details,ami_details
from rds_details import rds_details,rds_instance_details
from opswork_details import opswork_details, opswork_instance_details
from dynamodb_details import dynamodb_details,table_details
from redshift_details import redshift_details, cluster_details
from emr_details import emr_details,emr_cluster_details

def main():

    profiles = ['dev','stag','pre-prod','prod']

    for p in profiles:
        print '#######################################'
        print '#############%s###################'%p
        print '#######################################'

        ## Common session for each profile
        common_client = aws_session(p)

        ############### EC2  #####################

        ## ec2 connection for all instances
        cli = ec2_details(common_client.session)

        ### instances ###
        ## Getting all instance in a profile

        instance = cli.get_instances()

        notify = 0
        print 'Fetching EC2 instance without project tag'
        for i in instance:
            for j in i['Reservations']:
                if j['Instances'][0]['State']['Name'] == 'running':
                    in_de = instance_details(j)

                    if in_de.project == '':
                        print in_de.id
                        notify = 1

        if notify == 0:
            print 'None'

        ### instances ###


        ## EBS VOLUME ##
        notify = 0
        print 'Fetching EBS volumes without project tag'
        volumes = cli.get_volumes()

        for vols in volumes:
            vol_de =  volume_details(vols)
            if vol_de.project == '':
                print vol_de.id
                notify = 1

        if notify == 0:
            print 'None'

        ## EBS VOLUME ##


        ## EBS SNAPSHOT ##

        notify = 0
        print 'Fetching EBS snapshots without project tag'
        snapshots = cli.get_snapshots()
        for snap in snapshots:
            snap_de = snapshot_details(snap)
            if snap_de.project == '':
                print snap_de.id
                notify = 1
        if notify == 0:
            print 'None'

        ## EBS SNAPSHOT ##

        ## AMI ##

        notify = 0
        print 'Fetching AMIs without project tag'
        amis = cli.get_amis()
        for ami in amis:
            ami_de = ami_details(ami)
            if ami_de.project == '':
                print ami_de.id
                notify =1

        if notify == 0:
            print 'None'

        ## AMI ##

        ############### EC2  #####################




        ################ RDS  ###################
        rds_cli = rds_details(common_client.session)

        ## Getting all RDS instance in a profile

        rds_instance = rds_cli.get_instances()
        # out = rds_instance['DBInstances']

        notify = 0
        print 'Fetching RDS instance without project tag'
        for vals in rds_instance:
            if len(vals['DBInstances']) > 0:
                out = vals['DBInstances']


                for r in out:
                    if r['DBInstanceStatus'] == 'available':
                        rds_de = rds_instance_details(r)

                        tag = rds_cli.get_tags(rds_de.arn)
                        rds_de.assign_tags(tag)

                        # print '%s-->%s'%(rds_de.name,rds_de.project)
                        # import sys;sys.exit()
                        if rds_de.project == '':
                            print rds_de.name
                            notify = 1




        if notify == 0:
            print 'None'
        ################ RDS  ###################

        ################ OpsWork  ###################

        ops_cli = opswork_details(common_client.session)

        ops_stacks = ops_cli.get_instances()
        # for s in ops_stacks['Stacks']:
        #     print s['Name']
        notify = 0
        print 'Fetching Opswork stacks without project tag'
        for outs in ops_stacks:
            if len(outs['Stacks']) > 0:
                for s in outs['Stacks']:
                    ops_de = opswork_instance_details(s)
                    # print ops_de.name
                    tags = ops_cli.get_tags(ops_de.arn)
                    # print tags
                    ops_de.assign_tags(tags)

                    if ops_de.project == '':
                        print ops_de.name
                        notify = 1

        if notify == 0:
            print 'None'

        ################ OpsWork  ###################

        ################  DynamoDB  ###################
        print 'Fetching DynamoDB without project tag'
        dynamo_cli = dynamodb_details(common_client.session)
        tables = dynamo_cli.get_instances()
        notify = 0
        for ta in tables:
            table_cli = table_details(ta)
            arn = dynamo_cli.get_arn(ta)
            tags = dynamo_cli.get_tags(arn)
            table_cli.assign_tags(tags)
            if table_cli.project == '':
                print table_cli.table
                notify = 1

        if notify == 0:
            print 'None'

        ################  DynamoDB  ###################

        ################  REDSHIFT  ###################

        print 'Fetching REDSHIFT without project tag'
        redshift_cli = redshift_details(common_client.session)
        clusters = redshift_cli.get_instances()
        notify = 0
        for c in clusters:
            clu_cli = cluster_details(c)
            if clu_cli.project == '':
                print clu_cli.name
                notify = 1

        if notify == 0:
            print 'None'


        ################  REDSHIFT  ###################

        ################  EMR  ###################

        print 'Fetching EMR without project tag'
        emr_cli = emr_details(common_client.session)
        clusters = emr_cli.get_instances()
        notify = 0
        for cu in clusters:
            cu_cli = emr_cluster_details(cu)
            tags = emr_cli.get_tags(cu_cli.id)
            cu_cli.assign_tags(tags)
            if cu_cli.project == '':
                print '%s-%s'%(cu_cli.id,cu_cli.name)
                notify = 1
        if notify == 0:
            print 'None'

        ################  EMR  ###################


if __name__ == '__main__':
    main()
