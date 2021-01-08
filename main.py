# Created by Elvis Xiang
# Randomly Plays Boss Music
# This is terrible code, please do not try and replicate it

# Change these variables

# These are in seconds
MinLength = 10800
MaxLength = 25200


# Bad Code
import time, random
from playsound import playsound
import pyttsx3
tts = pyttsx3.init()

while True:
    # Start Program
    tts.say('Startup Complete')
    tts.runAndWait()

    # Wait 3-7 hours
    time.sleep(random.randint(MinLength, MaxLength))
    tts.say('Why do i hear boss music?')
    tts.runAndWait()
    playsound('./Music/Boss1.wav')

