from flask import Flask,render_template,url_for,request,jsonify,redirect
from gtts import gTTS
from formTTS import GtextToSpeech,ZtextToSpeech
import os,requests,json,time
import secrets
a = {}
app = Flask(__name__)

app.config['SECRET_KEY'] ='asf'


@app.route('/',methods=['GET','POST'])
def home():
	form = GtextToSpeech() 
	return render_template('index.html',form=form)

@app.route('/zalo',methods=['GET','POST'])
def zalo():
	form = ZtextToSpeech()
	return render_template("zalo.html",form=form)

@app.route('/postData',methods=['POST']) 
def postData():
	random_hex = secrets.token_hex(8)
	#data = request.form.to_dict(flat=False)
	data1 = request.json
	text = data1['text']
	lang = data1['lang']
	tts = gTTS(text,lang=lang,slow=False)
	file = random_hex + '.mp3'
	tts.save('static/'+file)
	dir_file = url_for('static',filename=file)
	print('done')
	return jsonify({"dir":dir_file})


def download_file(link,url):
	with open(url, "wb") as file:
		response = requests.get(link)
		file.write(response.content)
	return 0

def getVoice(api_key,voice_id,speed,text):
	#api_key = '0E0I2OkOHIRjppXsnXpu9qEUg2Hocfvm'
	#voice_id = 2
	#speed = 1.0
	encode_type = 1
	#text = 'Xin chào mọi người. Cảm ơn mọi người đã đến đây'
	url = 'https://api.zalo.ai/v1/tts/synthesize'

	#Header
	header_parameters = {'apikey': api_key}
	#Body
	data = {'input': text.encode('utf-8'), 'speed': speed, 'encoder_type': encode_type,'speaker_id': voice_id}
	#Post
	response = requests.post(url, data = data, headers = header_parameters)
	url_file = response.json()['data']['url']
	return url_file



@app.route("/ZpostData", methods=['POST'])
def ZpostData():
	data = request.json
	api = data['api']
	text = data['text']
	speaker_id = data['speaker_id']
	speed = data['speed']
	link = getVoice(api,speaker_id,speed,text)
	#print(link)
	time.sleep(2)
	#random_hex = secrets.token_hex(8)
	#file = random_hex + '.mp3'
	#download_file(link,'static/'+file)
	#dir_file = url_for('static',filename=file) 
	print("done")
	dir_file = link
	return jsonify({"dir" : dir_file})




if __name__ == '__main__':
    app.run(debug=True)
	