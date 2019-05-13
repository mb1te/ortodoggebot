import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def send_to_telegram(event):
	data = {'chat_id' : '@ortoblogge', 'text' : event.object.text} #id канала
	url = 'https://api.telegram.org/bot745619680:AAFlpDDvR8eEUP3hg2H-VHy9I-c1XlU72NU/sendMessage'
	requests.get(url, params=data)

vk_session = vk_api.VkApi(token='bf9c9e8265613a6cc6b49352f4f5586433dcc487bf17d155f92ffa450132c6b848054e3404fd6eacd156b')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '150420788') #id группы

for event in longpoll.listen():
	if event.type == VkBotEventType.WALL_POST_NEW and event.object['from_id'] == -150420788:
		send_to_telegram(event)