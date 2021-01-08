# Created by Elvis Xiang
# Randomly Plays Boss Music
# This is terrible code, please do not try and replicate it

import time, random
from playsound import playsound
import pyttsx3

tts = pyttsx3.init()

while True:
    # Start Program
    tts.say('Startup Complete')
    tts.runAndWait()

    # Wait 3-7 hours
    time.sleep(random.randint(3, 7) * 3600)
    tts.say('Why do i hear boss music?')
    tts.runAndWait()
    playsound('./Music/Boss1.wav')

