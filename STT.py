import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:  # run mic
    print('Listening...')
    audio = r.listen(source)  # store sound in var audio

try:
    text = r.recognize_google(audio, language='en-US')
    print(text)
except sr.UnknownValueError:
    print('Can not listen.')  # fail listening
except sr.RequestError as e:
    print("request error:{}".format(e))
