from pytube import YouTube
from moviepy.editor import *

# Link do vídeo que deseja baixar
link = input('Qual vídeo você deseja baixar? ')

# Cria uma instância do objeto YouTube
yt = YouTube(link)


# Obtém a melhor qualidade de áudio disponível
audio = yt.streams.filter(only_audio=True).first()

# Baixa o arquivo de áudio em formato mp4
audio_file = audio.download()

# Converte o arquivo de áudio para mp3
print('Convertendo seu vídeo em áudio')
mp3_file = audio_file.split('.')[0] + '.mp3'
AudioFileClip(audio_file).write_audiofile(mp3_file)

# Remove o arquivo de áudio em formato mp4
os.remove(audio_file)
print('Finalizado com sucesso')