import requests
from tgmsg.models import *
def sendTg(question_name,link):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)  # забираем первый объект из telesettings
        token = str(settings.tg_token)  # подставляем значение полей объекта
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        # print('имя вопроса',question_name)

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
                part_1 = text[0:text.find('{')]
                part_2 = text[text.find('}') + 1:text.rfind('{')]
                text_slize = part_1 + str(question_name) + '\n' + part_2 + link
                print(link)
        else:
            text_slize = text
        r = requests.post(method, data={
            "chat_id": chat_id,
            "text": text_slize,

        })
        # print(text_slize)
        # print(r.text)
        if r.status_code != 200:
            raise Exception("post_text error")




