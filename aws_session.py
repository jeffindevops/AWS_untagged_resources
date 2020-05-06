import boto3

class aws_session:
    def __init__(self,profile):
        self.profile = profile
        self.session = ''

        try:
            self.session = boto3.session.Session(profile_name=self.profile)
            # print 'EC2 connection Session successfully created for %s' % self.profile

        except:
            print "Error :- Can't create session with given profile -->%s"%self.profile