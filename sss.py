from insm import *
from batt import *
#from mys import *
###############
#print(botmm)
bot = telebot.TeleBot(botmm)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, """    السلام عليكم ورحمه الله وبركاته
في هذا البوت هذا البوت مطوره عمر ستايل😎😍
هذا البوت ماذا يفعل او ماذا عمله او شغله هذا البوت ينزل فيديوهات او صور من الانستا

# مثال
كيف يعمل هذا البوت هذا البوت فقط للانستا يعني ترى فيديو على الانستا هات رابط الفيديو ووضع في البوت وسيتم تحميل الفيديو او او صوره على الانستا تحب ان تنزلها اضع رابط الصوره في البوت وسيتم تنزيل هذه الصوره

###############
ملاحظه الرجاء اذا لم يتم الاشتغال هذا البوت🙏🙏😢
قصدي كيف يعني اذا انت وضعت الرابط ولم يتم تنزيل هذا الفيديو او الصوره فالرجاء التواصل معنا على حساباتنا الاخرى

@OmarStyle1
@Kaouterbekraoui
https://t.me/omarstyle12
https://t.me/chatadowat
https://t.me/BGX4_2 
https://t.me/toxiccode12
""")
#       m =bot.reply_to(message)
#       if m == "omar":
#               bot.reply_to(message,"ok ok")
@bot.message_handler(func=lambda ms: True)
###################~########
##################
def echo_all(ms):
######
        #omar(message)
	#emil(ms)
	rmm(ms)
####
bot.infinity_polling()
