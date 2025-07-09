###[스트링 읽기]##############################
from gtts import gTTS
from playsound import playsound

file_name = "tts_ko_2.mp3"

# tts (ko)
txt = "엄마야 누나야 강변살자."
tts_ko = gTTS(text=txt, lang='ko')
tts_ko.save(f"chat_bot/x_tts/{file_name}")
playsound(f"chat_bot/x_tts/{file_name}")

# ###[파일 읽기 + pygame 사용하기]#############

# from gtts import gTTS
# import pygame    # pip install pygame
# import time
# import os

# file_name = "tts_ko_2.mp3"
# file_path = os.path.abspath(f"chat_bot/x_tts/{file_name}")

# # 파일 텍스트 읽기
# with open('chat_bot/x_tts/ptScript.txt', 'r', encoding='utf8') as f:
#     txt = f.read()

# tts_ko = gTTS(text=txt, lang='ko')
# tts_ko.save(file_path)

# # pygame을 사용하여 오디오 파일 재생
# pygame.mixer.init()
# pygame.mixer.music.load(file_path)
# pygame.mixer.music.play()

# # 재생이 끝날 때까지 기다림
# while pygame.mixer.music.get_busy():
#     time.sleep(1)

