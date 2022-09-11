from flask import Flask, jsonify, render_template import pprint import requests

PROFILES = { 'ed': '6eUKZXaKkcviH0Ku9w2n3V', }

pp = pprint.PrettyPrinter(indent=1)

app = Flask(name)

data = { 'artists':[ { 'external_urls' : { 'spotify' : 'link.com' }, 'followers' : { 'href' : None, 'total' : 10238 }, 'genres' : [{ '0' : 'pop', '1' : 'uk pop'}], 'id' : 'ed', 'images':[ {'url' : 'url.com'}, {'url' : 'url.com'}], 'name' : 'ed sheeran'

}
]

}

songs = data['artists'][0]
print(songs['followers'])
print(songs['genres'])
print(songs['images'])
print(songs['name'])
@app.route('/') def index(): url = "https://spotify23.p.rapidapi.com/artists/" querystring = {"ids":PROFILES['ed']} headers = { "X-RapidAPI-Key": "d4a3a53a35msh7bda5416a505459p13b933jsn53af9f0b28a1", "X-RapidAPI-Host": "spotify23.p.rapidapi.com" } response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json() contents = data['artists'] print(contents) songs = data['artists'] return 'home_page'

app.run(host='0.0.0.0', port=81)
