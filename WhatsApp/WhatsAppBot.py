from typing import List

import pywhatkit
import keyboard
import pyautogui
import time


class WhatsAppBot(object):
    @staticmethod
    def send_message(message: str, phones: List[str]):
        for phone in phones:
            pywhatkit.whats.sendwhatmsg_instantly(phone, message + ' 🥳', 8)
            pyautogui.click(850, 850)
            time.sleep(1.5)
            keyboard.press_and_release('enter')
