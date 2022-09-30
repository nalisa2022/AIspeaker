import time
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

# use STT


def listen(recognizer, audio):

    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print("[Human]", text)
        answer(text)
    except sr.UnknownValueError:
        print('Can not listen.')  # fail listening
    except sr.RequestError as e:
        print("request error:{}".format(e))

# use TTS


def answer(input_text):
    answer_text = ''
    if 'hello' in input_text:
        answer_text = 'hello'
    speak(answer_text)


def speak(text):
    print('[AI]', text)
    file_name = 'voice.mp3'
    tts_en = gTTS(text=text, lang='en')
    tts_en.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()

speak('what can i do for you?')

# m-> listen,  listen-> call func, (listen and speak)
stop_listen = r.listen_in_background(m, listen)
# stop_listen(wait_for_stop=False) # stop listening

while True:
    time.sleep(0.1)
