# 제 2차: 마이크 입력 음성 인식
import speech_recognition as sr

# 마이크로 음성 입력
recog = sr.Recognizer()
with sr.Microphone() as source:
    print('1초 후에 말하세요.')
    audio = recog.listen(source)

# # 마이크 없이 음성파일로 입력(허용형식: wav, aiff/aiff-c, flac, (mp3: 불가))
# recog = sr.Recognizer()
# with sr.AudioFile(r'chat_bot\x_tts\tts_ko_2.wav') as source:
#     audio = recog.record(source)

try:
    # 구글 API로 인식 (API key가 없으면 하루 50회만 사용 가능.)
    # txt = recog.recognize_google(audio, language='en-US')
    txt = recog.recognize_google(audio, language='ko')
    print(txt)

except sr.UnknownValueError:
    print('음성 인식 실패')
except sr.RequestError:
    print('요청 실패: {}'.format(100))  # API Key 오류. 네트워크 단절 등