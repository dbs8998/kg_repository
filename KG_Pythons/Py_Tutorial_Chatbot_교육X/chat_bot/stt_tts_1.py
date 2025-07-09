# 제 1차: 텍스트 - 음성 상호 변환
# pip install gTTS
# pip install playsound
# pip install SpeechRecognition
# pip install PyAudio  # 마이크 사용용

from gtts import gTTS

# tts (en)
txt = "How nice to see you, Hawx!"
file_name = "tts_en_1.mp3"
tts_en = gTTS(text=txt, lang='en')
tts_en.save(f"chat_bot/x_tts/{file_name}")

# mp3 파일 재생
from playsound import playsound
playsound("chat_bot/x_tts/tts_en_1.mp3")

