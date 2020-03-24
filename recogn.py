# https://realpython.com/python-speech-recognition/


import speech_recognition as sr     # import the library
import voice

def listen():
    """
    Listen to a microfone and try to recognize the words.
    :param: None
    :returns: The text heard.
    :raises: None so far.
    
    """
    text = 'não entendi.Repita!'
    r = sr.Recognizer()                 # initialize recognizer
    r.energy_threshold = 5000
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio, language='pt-BR')    # use recognizer to convert our audio into text part.         
        except:
            pass

    voice.speak(text)

while True:
    listen()
