from gtts import gTTS
from playsound import playsound

audio = 'audio-gerado.mp3' 
language = 'pt-br'

try:
    transform = gTTS (
        text = 'gerando um audio atraves de texto com Python',
        lang = language
    )

    transform.save(audio)
    playsound(audio)
except:
    print('erro...')