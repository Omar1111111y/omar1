###
import os
import random
import requests
import json
from insm  import * 
#from tkinter import filedialog
bot = telebot.TeleBot(botmm)
def rmm(ms):
	
	iff = ms.text

	url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

	postUrl = iff

	querystring = {"url": postUrl}

	headers = {
   	'x-rapidapi-host': "instagram-media-downloader.p.rapidapi.com",
    	'x-rapidapi-key': "a225514c66msh6db31d5d9409711p1a9d9ajsn46b7f1221bf5" # Put Your API Key
    	}
#	try:
	response = requests.request("GET", url, headers=headers, params=querystring)

	textToJson = json.loads(response.text)
#        print(textToJson)
#	except TypeError:
#		bot.reply_to(ms,"Eellllll")
	try:
		postFileUrl = ''

		if 'video' in textToJson:
    			postFileUrl = textToJson["video"]
		else: postFileUrl = textToJson["image"]

		reqPostFileUrl = requests.get(postFileUrl)

		fileEx = reqPostFileUrl.headers['Content-Type'].split('/')[-1].split('.')[0]
		lst = "kamsmsmkwkekw0202030o2kksa"
		vv = str(''.join((random.choice(lst) for i in range(7))))
		fileName = "/sdcard/mip/ddd"+'/'+vv+'.' + fileEx
	
		with reqPostFileUrl as rq:
			with open(fileName, 'wb') as file:
				file.write(rq.content)
		#		bot.reply_to(ms,'جاري تحميل الصوره او الفيديو')
				if fileEx == "jpeg" or fileEx == "png":
					bot.reply_to(ms,'جاري تحميل الصوره')
					bot.send_photo(ms.chat.id,open(fileName,"rb"))
					os.remove(fileName) #rm
				elif fileEx == 'mp4':
					bot.reply_to(ms,'جاري تحميل الفيديو')
					bot.send_video(ms.chat.id,open(fileName,"rb"))
					os.remove(fileName) #rm 
					bot.reply_to(ms,'مطور هذا البوت عمر ستايل')
				else:
					bot.reply_to(ms,"""خطا الرجاء تواصل مع عمر ستايل وبعث له الرابط😢😢😢😭@OmarStyle1""")
	except KeyError:
		#bot.reply_to(ms,pass)
		pass
	except TypeError:
		bot.reply_to(ms,"""
للاسف يوجد خطا في الرابط الرجاء التاكد من الرابط

#مثل 
مثال اذا انت كنت متاكد من هذا الرابط انه صحيح الرجاء تواصل معنا
@OmarStyle1
👍😎@OmarStyle1""")
