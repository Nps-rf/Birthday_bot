from typing import List

import pywhatkit
import keyboard
import pyautogui
import time
import json
import requests
from env import *


class WhatsAppBot(object):
    APIUrl = APIUrl
    token = token
    headers = {'Content-type': 'application/json'}

    @staticmethod
    def send_message_manual(message: str, phones: List[str]):
        for phone in phones:
            pywhatkit.whats.sendwhatmsg_instantly(phone, message + ' 🥳', 8)
            pyautogui.click(850, 850)
            time.sleep(1.5)
            keyboard.press_and_release('enter')

    @classmethod
    def send_message(cls, message: str, phones: List[str]):
        url = cls.APIUrl.format(cls.token)
        for phone in phones:
            data = {
                "phone": phone,
                "body": message
                       }
            answer = requests.post(url, data=json.dumps(data), headers=cls.headers)
            return answer.json()

