# Finding untagged resources

This script will look through all the profiles in the list and check if specific tag is assigned for resource. This will help you to identify untagged resource in AWS.

Tags are very usefull for cost calculation in cost expoloer

# Usage

You can specify the profiles ( aws profiles configured in machine ) in script.

### Run command

``` bash
/usr/bin/python main.py

```


### Config values
1.) profiles :- aws profiles as a list. Main will loop through all profiles added in this value
    Example :- ['prod','stag','dev']
    
2.) tag :- Finding resources don't have this tag
    Example :- environment
    Example :- client
