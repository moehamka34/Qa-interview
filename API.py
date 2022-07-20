import urllib.request, json
from collections import OrderedDict
#urllib is for http requests, for get and post
#only include request function as that's the only one that we need for this program



with urllib.request.urlopen("https://randomuser.me/api") as url:    # get request for url
    data = json.loads(url.read().decode())                          # present it as JSON
    key_json = (data['results'][0].keys())                          # save 'names'


value = 1                                                       # initialize 'value'
with open('json_data.json', 'w') as outfile:                    # open JSON file
    for key in reversed(key_json):                              # loop through names
        json_dt = {}                                            # initialize JSON object
        json_dt['name'] = (data['results'][0][key])   # store value of cur. name in object
        json_dt['value'] = (value)                             # store current value    
        json.dump(json_dt,outfile)                             # export object to JSON
        value = value+1                                     # increase value for next obj


