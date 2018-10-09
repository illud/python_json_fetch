import urllib, json

url = "https://facebook.github.io/react-native/movies.json"

response = urllib.urlopen(url)

data = json.loads(response.read())

print data
