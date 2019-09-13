import requests
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def send_to_telegram(event):
	data = {'chat_id' : '@ortoblogge', 'text' : event} #id канала
	url = 'https://api.telegram.org/bot745619680:AAFlpDDvR8eEUP3hg2H-VHy9I-c1XlU72NU/sendMessage'
	requests.get(url, params=data)

vk_session = vk_api.VkApi(token='bf9c9e8265613a6cc6b49352f4f5586433dcc487bf17d155f92ffa450132c6b848054e3404fd6eacd156b')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '150420788') #id группы


while True:
    try:
        for event in longpoll.listen():
                if event.type == VkBotEventType.WALL_POST_NEW and event.object['from_id'] == -150420788:
                    print("successful", time.ctime())
                    if len(event.object.text) > 4096:
                        t = event.object.text.split('\n')
                        msg = ''
                        for i in t:
                            if len(msg) + len(i) + 1 < 4096:
                                msg = msg + i + "\n"
                            else:
                                send_to_telegram(msg)
                                msg = i + "\n"
                        send_to_telegram(msg)
                    else:
                        send_to_telegram(event.object.text)

    except:
        print("failed", time.ctime())
