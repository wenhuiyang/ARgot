# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()
# -*- coding: utf-8 -*-
import requests
import json
import os

from flask import Flask, jsonify
from google.cloud import translate
from watson_developer_cloud import TextToSpeechV1



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./apiKey/ARgot-2901c81d1cd3.json"

app_id = 'e299e0de'
app_key = '3ac35902b6dcfa9e855f892dd0f68665'

source_language = 'en'
target_language = 'es'

text_to_speech = TextToSpeechV1(
    username='eb37ff04-83a6-4172-82a2-24adaa022c2b',
    password='w1tqUEEyau5C',
    x_watson_learning_opt_out=True)

app = Flask(__name__)      
 
@app.route('/')
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/<string:word>', methods=['GET'])
def getTranslation(word):
	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + source_language + '/' + word.lower() + '/translations=' + target_language
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	print("code {}\n".format(r.status_code))
	#print("json \n" + json.dumps(r.json()))
	translation = translate_text(word)
	read_text(translation)
	return jsonify({'message' : r.json()});



@app.route('/favicon.ico', methods=['GET'])
def favicon():
	return jsonify({'message' : 'favicon'})

def translate_text(text, target='es'):
	translate_client = translate.Client()
	result = translate_client.translate(text, target_language=target)

	return result['translatedText']

def read_text(word):
	with open('./output.mp3',
	          'wb') as audio_file:
	    audio_file.write(
	        text_to_speech.synthesize(word, accept='audio/mp3',
	                                  voice="es-US_SofiaVoice"))

 
if __name__ == '__main__':
  app.run(debug=True, port=8080)

