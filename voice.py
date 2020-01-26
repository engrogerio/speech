from gtts import gTTS
from io import BytesIO
import subprocess


def play_file(file_name):
    bashCommand = 'play %s' % file_name
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def speak(text):
    file_name = '.voice.mp3'
    tts_pt = gTTS(text, lang='pt-BR')
    # mp3_fp = file_name
    tts_pt.save(file_name)
    play_file(file_name)


if __name__ == "__main__":
    file_name = '/home/rogerio/invent/speech/test.mp3'
    text = 'Funciona, Rogério. Parabens'
    speak(text, file_name)
