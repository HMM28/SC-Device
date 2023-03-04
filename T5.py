                                                                                                                                                                                                              
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import playsound
from pygame import mixer
#Code for button#
import RPi.GPIO as GPIO
import time
import os
import sys
#Code for button#

mixer.init()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)

#Code for button#
GPIO.setmode(GPIO.BCM)
GPIO.setup(2 ,GPIO.IN)
prev_input = 1
#Code for button#

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:

    with sr.Microphone() as source:
        print('You can speak now')
        talk("You can speak now")
        listener.phrase_threshold = 2
        audio = listener.listen(source, phrase_time_limit=3)
        command = listener.recognize_google(audio)
        text = command
        speech = gTTS(text=text, lang="en", slow=False, )
        speech.save("texttospeech.mp3")
    print(command)

    if command == "hello":
        print("magandang umaga")
        tts = gTTS(text="magandang umaga", lang="tl")
        filename="magandangumaga.mp3"
        tts.save("magandangumaga.mp3")
        mixer.music.load("magandangumaga.mp3")
        mixer.music.play()
    if command == "mga ng":
        print("magandang umaga")
        tts = gTTS(text="magandang umaga", lang="tl")
        filename="magandangumaga.mp3"
        tts.save("magandangumaga.mp3")
        mixer.music.load("magandangumaga.mp3")
        mixer.music.play()

    if command == "mola":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "mala":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "moya":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "maya":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "moira":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "maria":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "moa":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "maja":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    if command == "moana":
        print("bola")
        tts = gTTS(text="bola", lang="tl")
        filename="bola.mp3"
        tts.save("bola.mp3")
        mixer.music.load("bola.mp3")
        mixer.music.play()
    
    if command == "salamat po":
        print("salamat po")
        tts = gTTS(text="salamat po", lang="tl")
        filename="salamatpo.mp3"
        tts.save("salamatpo.mp3")
        mixer.music.load("salamatpo.mp3")
        mixer.music.play()
    if command == "alamat":
        print("salamat po")
        tts = gTTS(text="salamat po", lang="tl")
        filename="salamatpo.mp3"
        tts.save("salamatpo.mp3")
        mixer.music.load("salamatpo.mp3")
        mixer.music.play()
    if command == "alamat ng":
        print("salamat po")
        tts = gTTS(text="salamat po", lang="tl")
        filename="salamatpo.mp3"
        tts.save("salamatpo.mp3")
        mixer.music.load("salamatpo.mp3")
        mixer.music.play()
    if command == "alamat mo":
        print("salamat po")
        tts = gTTS(text="salamat po", lang="tl")
        filename="salamatpo.mp3"
        tts.save("salamatpo.mp3")
        mixer.music.load("salamatpo.mp3")
        mixer.music.play()
    if command == "alarm at":
        print("salamat po")
        tts = gTTS(text="salamat po", lang="tl")
        filename="salamatpo.mp3"
        tts.save("salamatpo.mp3")
        mixer.music.load("salamatpo.mp3")
        mixer.music.play()

    if command == "ngayon alawan":
        print("maligayang kaarawan")
        tts = gTTS(text="maligayang kaarawan", lang="tl")
        filename="maligayaang kaarawan.mp3"
        tts.save("maligayang kaarawan.mp3")
        mixer.music.load("maligayang kaarawan.mp3")
        mixer.music.play()
    if command == "maligayang kaarawan":
        print("maligayang kaarawan")
        tts = gTTS(text="maligayang kaarawan", lang="tl")
        filename="maligayaang kaarawan.mp3"
        tts.save("maligayang kaarawan.mp3")
        mixer.music.load("maligayang kaarawan.mp3")
        mixer.music.play()
    if command == "halimbawa ng one":
        print("maligayang kaarawan")
        tts = gTTS(text="maligayang kaarawan", lang="tl")
        filename="maligayaang kaarawan.mp3"
        tts.save("maligayang kaarawan.mp3")
        mixer.music.load("maligayang kaarawan.mp3")
        mixer.music.play()
    if command == "maniwaya awan":
        print("maligayang kaarawan")
        tts = gTTS(text="maligayang kaarawan", lang="tl")
        filename="maligayaang kaarawan.mp3"
        tts.save("maligayang kaarawan.mp3")
        mixer.music.load("maligayang kaarawan.mp3")
        mixer.music.play()
    if command == "mangayawan":
        print("maligayang kaarawan")
        tts = gTTS(text="maligayang kaarawan", lang="tl")
        filename="maligayaang kaarawan.mp3"
        tts.save("maligayang kaarawan.mp3")
        mixer.music.load("maligayang kaarawan.mp3")
        mixer.music.play()

    if command == "ama":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "amo":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "ama pa":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "mama":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "pa":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "paa":
        print("kamusta")
        tts = gTTS(text="kamusta ka", lang="tl")
        filename="kamustaka.mp3"
        tts.save("kamustaka.mp3")
        mixer.music.load("kamustaka.mp3")
        mixer.music.play()
    if command == "i mean":
        print("pagkain")
        tts = gTTS(text="pagkain", lang="tl")
        filename = "pagkain.mp3"
        tts.save("pagkain.mp3")
        mixer.music.load("pagkain.mp3")
        mixer.music.play()
        
    if command == "no":
        print("lugar")
        tts = gTTS(text="lugar", lang="tl")
        filename = "lugar.mp3"
        tts.save("lugar.mp3")
        mixer.music.load("lugar.mp3")
        mixer.music.play

    if command == "yow":
        print("lugar")
        tts = gTTS(text="lugar", lang="tl")
        filename = "lugar.mp3"
        tts.save("lugar.mp3")
        mixer.music.load("lugar.mp3")
        mixer.music.play()
        
    if command == "no no":
        print("lugar")
        tts = gTTS(text="lugar", lang="tl")
        filename = "lugar.mp3"
        tts.save("lugar.mp3")
        mixer.music.load("lugar.mp3")
        mixer.music.play()

    if command == "yoyo":
        print("lugar")
        tts = gTTS(text="lugar", lang="tl")
        filename = "lugar.mp3"
        tts.save("lugar.mp3")
        mixer.music.load("lugar.mp3")
        mixer.music.play()

        
    if command == "royale":
        print("lugar")
        tts = gTTS(text="lugar", lang="tl")
        filename = "lugar.mp3"
        tts.save("lugar.mp3")
        mixer.music.load("lugar.mp3")
        mixer.music.play()

    if command == "nanay":
        print("bagay")
        tts = gTTS(text="bagay", lang="tl")
        filename = "bagay.mp3"
        mixer.music.load("bagay.mp3")
        mixer.music.play()

    if command == "mamay":
        print("bagay")
        tts = gTTS(text="bagay", lang="tl")
        filename = "bagay.mp3"
        tts.save("bagay.mp3")
        mixer.music.load("bagay.mp3")
        mixer.music.play()
        
    if command == "mama":
        print("bagay")
        tts = gTTS(text="bagay", lang="tl")
        filename = "bagay.mp3"
        tts.save("bagay.mp3")
        mixer.music.load("bagay.mp3")
        mixer.music.play
        
    if command == "mamaya":
        print("bagay")
        tts = gTTS(text="bagay", lang="tl")
        filename = "bagay.mp3"
        tts.save("bagay.mp3")
        mixer.music.load("bagay.mp3")
        mixer.music.play()
        
    if command == "kulay":
        print("kulay")
        tts = gTTS(text="kulay", lang="tl")
        filename = "kulay.mp3"
        tts.save("kulay.mp3")
        mixer.music.load("kulay.mp3")
        mixer.music.play()
        
    if command == "kulang":
        print("kulay")
        tts = gTTS(text="kulay", lang="tl")
        filename = "kulay.mp3"
        tts.save("kulay.mp3")
        mixer.music.load("kulay.mp3")
        mixer.music.play()
        
    if command == "kulam":
        print("kulay")
        tts = gTTS(text="kulay", lang="tl")
        filename = "kulay.mp3"
        tts.save("kulay.mp3")
        mixer.music.load("kulay.mp3")
        mixer.music.play()
        
    if command == "newline":
        print("gulay")
        tts = gTTS(text="gulay", lang="tl")
        filename = "gulay.mp3"
        tts.save("gulay.mp3")
        mixer.music.load("gulay.mp3")
        mixer.music.play()
        
    if command == "luna":
        print("gulay")
        tts = gTTS(text="gulay", lang="tl")
        filename = "gulay.mp3"
        tts.save("gulay.mp3")
        mixer.music.load("gulay.mp3")
        mixer.music.play()
        

    if command == "lunan":
        print("gulay")
        tts = gTTS(text="gulay", lang="tl")
        filename = "gulay.mp3"
        tts.save("gulay.mp3")
        mixer.music.load("gulay.mp3")
        mixer.music.play()
        
    if command == "nolan":
        print("gulay")
        tts = gTTS(text="gulay", lang="tl")
        filename = "gulay.mp3"
        tts.save("gulay.mp3")
        mixer.music.load("gulay.mp3")
        mixer.music.play()
        
    if command == "lunan":
        print("gulay")
        tts = gTTS(text="gulay", lang="tl")
        filename = "gulay.mp3"
        tts.save("gulay.mp3")
        mixer.music.load("gulay.mp3")
        mixer.music.play()
        
    if command == "puta":
        print("prutas")
        tts = gTTS(text="prutas", lang="tl")
        filename = "prutas.mp3"
        tts.save("prutas.mp3")
        mixer.music.load("prutas.mp3")
        mixer.music.play()
        
    if command == "kuwago":
        print("pwede")
        tts = gTTS(text="pwede", lang="tl")
        filename = "pwede.mp3"
        tts.save("pwede.mp3")
        mixer.music.load("start pwede.mp3")
        mixer.music.play()
        
    if command == "pwede":
        print("pwede")
        tts = gTTS(text="pwede", lang="tl")
        filename = "pwede.mp3"
        tts.save("pwede.mp3")
        mixer.music.load("pwede.mp3")
        mixer.music.play
        
    if command == "huwag":
        print("pwede")
        tts = gTTS(text="pwede", lang="tl")
        filename = "pwede.mp3"
        tts.save("pwede.mp3")
        mixer.music.load("pwede.mp3")
        mixer.music.play()
        
    if command == "weather":
        print("pwede")
        tts = gTTS(text="pwede", lang="tl")
        filename = "pwede.mp3"
        tts.save("pwede.mp3")
        mixer.music.load("pwede.mp3")
        mixer.music.play()
        
    if command == "panda":
        print("hinde")
        tts = gTTS(text="hinde", lang="tl")
        filename = "hinde.mp3"
        tts.save("hinde.mp3")
        mixer.music.load("hinde.mp3")
        mixer.music.play()
        
    if command == "honda":
        print("hinde")
        tts = gTTS(text="hinde", lang="tl")
        filename = "hinde.mp3"
        tts.save("hinde.mp3")
        mixer.music.load("hinde.mp3")
        mixer.music.play()
        
    if command == "meron":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "leron":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "ryan":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "lauren":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "melon":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "mamon":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "naman":
        print("meron")
        tts = gTTS(text="meron", lang="tl")
        filename = "meron.mp3"
        tts.save("meron.mp3")
        mixer.music.load("meron.mp3")
        mixer.music.play()
        
    if command == "meow":
        print("dilaw")
        tts = gTTS(text="dilaw", lang="tl")
        filename = "dilaw.mp3"
        tts.save("dilaw.mp3")
        mixer.music.load("dilaw.mp3")
        mixer.music.play()
        
    if command == "bilao":
        print("dilaw")
        tts = gTTS(text="dilaw", lang="tl")
        filename = "dilaw.mp3"
        tts.save("dilaw.mp3")
        mixer.music.load("dilaw.mp3")
        mixer.music.play()
        
    if command == "noun":
        print("dilaw")
        tts = gTTS(text="dilaw", lang="tl")
        filename = "dilaw.mp3"
        tts.save("dilaw.mp3")
        mixer.music.load("dilaw.mp3")
        mixer.music.play()
        
    if command == "london":
        print("berde")
        tts = gTTS(text="berde", lang="tl")
        filename = "berde.mp3"
        tts.save("berde.mp3")
        mixer.music.load("berde.mp3")
        mixer.music.play()
        
    if command == "sound":
        print("berde")
        tts = gTTS(text="berde", lang="tl")
        filename = "berde.mp3"
        tts.save("berde.mp3")
        mixer.music.load("berde.mp3")
        mixer.music.play()
        
    if command == "download":
        print("berde")
        tts = gTTS(text="berde", lang="tl")
        filename = "berde.mp3"
        tts.save("berde.mp3")
        mixer.music.load("berde.mp3")
        mixer.music.play()

    if command == "good":
        print("food")
        tts = gTTS(text="food", lang="tl")
        filename = "food.mp3"
        tts.save("food.mp3")
        mixer.music.load("food.mp3")
        mixer.music.play()

    if command == "moon":
        print("food")
        tts = gTTS(text="food", lang="tl")
        filename = "food.mp3"
        tts.save("food.mp3")
        mixer.music.load("food.mp3")
        mixer.music.play()

    if command == "food":
        print("food")
        tts = gTTS(text="food", lang="tl")
        filename = "food.mp3"
        tts.save("food.mp3")
        mixer.music.load("food.mp3")
        mixer.music.play()
        
    if command == "horror":
        print("color")
        tts = gTTS(text="color", lang="tl")
        filename = "color.mp3"
        tts.save("color.mp3")
        mixer.music.load("color.mp3")
        mixer.music.play()
        
    if command == "person":
        print("person")
        tts = gTTS(text="person", lang="tl")
        filename = "person.mp3"
        tts.save("person.mp3")
        mixer.music.load("person.mp3")
        mixer.music.play()
except:
    tts = gTTS(text="error", lang="tl")
    filename = "error.mp3"
    tts.save("error.mp3")
    mixer.music.load("error.mp3")
    mixer.music.play()

#Code for button#
while True:
        input = GPIO.input(2)

        if ((not prev_input) and input):
            os.system("python /home/group4/Desktop/t5.py")

        prev_input = input

        time.sleep(.05)
#Code for button#
