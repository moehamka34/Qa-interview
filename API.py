import urllib.request, json
from collections import OrderedDict
#urllib is for http requests, for get and post
#only include request function as that's the only one that we need for this program

#json is to include it as json format

with urllib.request.urlopen("https://randomuser.me/api") as url:    # get request for url
    data = json.loads(url.read().decode())                          # present it as JSON
    key_json = (data['results'][0].keys())                          # display the results


value = 1
with open('json_data.json', 'w') as outfile:
    for key in reversed(key_json):
        json_dt = {}
        json_dt['name'] = (data['results'][0][key])
        json_dt['value'] = (value)
        json.dump(json_dt,outfile)
        value = value+1


