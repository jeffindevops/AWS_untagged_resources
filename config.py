conf = {
    'profiles':['dev','stag','pre-prod','prod'], # profiles which using to check the resources
    'tag':'PROJECT',  # searching for specific tag key
}



# conf pre checks
if not isinstance(conf['profiles'], list) and len(conf['profiles']) < 1:
    print 'Please add profiles as non empty list..'
    print 'Exiting...'
    exit()


if not isinstance(conf['tag'], str) and len(conf['tag']) < 1:
    print 'Please provide tag value as a non empty string.'
    print 'Exiting...'
    exit()
