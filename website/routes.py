# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()

import requests
import json

from flask import Flask, jsonify

app_id = 'e299e0de'
app_key = '3ac35902b6dcfa9e855f892dd0f68665'

source_language = 'en'
target_language = 'es'

app = Flask(__name__)      
 
@app.route('/')
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/<string:word>', methods=['GET'])
def getTranslation(word):
	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + source_language + '/' + word.lower() + '/translations=' + target_language
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	print("code {}\n".format(r.status_code))
	print(word + '\n')
	print("text \n" + r.text)
	#print("json \n" + json.dumps(r.json()))
	return jsonify({'message' : 'abby'});



 
if __name__ == '__main__':
  app.run(debug=True, port=8080)