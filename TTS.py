from playsound import playsound
from gtts import gTTS


file_name = 'sample.mp3'

# text = 'Can I help you?'
with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)
playsound(file_name)  # play mp3 in program
