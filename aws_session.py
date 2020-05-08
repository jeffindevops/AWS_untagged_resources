import boto3

class aws_session:
    """
    Creating boto3 session with given profile
    """
    def __init__(self,profile):
        self.profile = profile
        self.session = ''

        try:
            self.session = boto3.session.Session(profile_name=self.profile)

        except:
            print "Error :- Can't create session with given profile -->%s"%self.profile
            print "Skipping to next profile"
