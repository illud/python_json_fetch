#import library's
import urllib, json
#create variable with url to fetch
url = "https://facebook.github.io/react-native/movies.json"
#get the response
response = urllib.urlopen(url)
#load response and save to data
data = json.loads(response.read())
#print json data
print data
#create a json file and write data
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
