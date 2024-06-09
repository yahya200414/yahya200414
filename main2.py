from requests import *
from flask import *
import requests
from json import dumps
import json
ya= Flask(__name__)	
@ya.route('/',methods=['GET'])
def yahya():
	try:
		url1=request.args.get('url')
	except:
		return json.dumps({"result":False,"error":True})
	if str('https://www.instagram.com/reel/') in str(url1):
		try:
			code=url1.split('/reel/')[1].split('/')[0]
		except:
			return json.dumps({"result":False,"error":True,"message":"your link not valid try another link"})
	elif str('https://www.instagram.com/p/') in str(url1):
		try:
			code=url1.split('/p/')[1].split('/')[0]
		except:
			return json.dumps({"result":False,"error":True,"message":"your link not valid try another link"})
	try:
		url=f'https://www.instagram.com/graphql/query/?doc_id=24852649951017035&variables=%7B%22shortcode%22%3A%22'+code+'%22%7D'
	except:
		pass
	head={"Accept-Encoding":"gzip",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"User-Agent":"Mozilla/5.0 (Linux; Android 12; SM-A025F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.179 Mobile Safari/537.36",
"Cookie":"csrftoken=IfQbcfvEx08G0FhGEGSayC",
"Host":"www.instagram.com",

"Connection":"Keep-Alive"
}
	try:
		r=requests.get(url,headers=head).json()['data']
		return json.dumps({"result":True,"error":False,"data":[r],"devloper":"yahya_almashhdany"})
	except:
		return json.dumps({"error_ai_info":True,"reuslt":None,"devloper":"yahya_almshhdany"})

ya.run(debug=True,host='0.0.0.0',port=9988)
	