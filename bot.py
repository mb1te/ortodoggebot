import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def send_to_telegram(event):
	data = {'chat_id' : '@testchannelmb1te', 'text' : event.object.text} #id канала
	url = 'https://api.telegram.org/bot745619680:AAFlpDDvR8eEUP3hg2H-VHy9I-c1XlU72NU/sendMessage'
	requests.get(url, params=data)
	if event.object.get('attachments', None) != None:
	#	print(event.object.attachments)
		for i in event.object.attachments:
			if (i['type'] == 'photo'):
				sz = 0
				imgurl = ''
				for j in i['photo']['sizes']:
					if j['width'] > sz:
						sz = j['width']
						imgurl = j['url']
				data = {'chat_id' : '@testchannelmb1te', 'photo' : imgurl} #id канала
				url = 'https://api.telegram.org/bot745619680:AAFlpDDvR8eEUP3hg2H-VHy9I-c1XlU72NU/sendPhoto'
				requests.get(url, params=data)
	

vk_session = vk_api.VkApi(token='c24e6c259f278867d66a4d110d4b42f3294e912b5f7fe26974a903b3133f5c0fb8cc685d3ad678d453c18')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '159003014') #id группы

for event in longpoll.listen():
	if event.type == VkBotEventType.WALL_POST_NEW:
		send_to_telegram(event)