# AI 스피커 만들기
# TTS(도움 원해?) > STT  > text 비교 > TTS 응대
# 날씨 정보 가져와서 알려주기.

import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from APIs import w_main as w
import sys

weather_now = w.weather_info()
temp = weather_now['current']['temp_c']
sky = weather_now['current']['condition']['text']

# 플래그 변수 설정
program_status = True

# STT
def listen(recognizer, audio):
    try:
        txt = recognizer.recognize_google(audio, language='ko')
        print('[나의 말] '+txt)
        reply(txt)
    except sr.UnknownValueError:
        print('음성인식 실패')
    except sr.RequestError as e:
        print('요청실패: {0}'.format(e)) 

# AI 응대
def reply(input_txt):
    global program_status
    answer_txt = ''
    if '안녕' in input_txt:
        answer_txt = '네. 좋은 아침이네요.'
    elif '날씨' in input_txt:
        answer_txt = f'오늘의 서울 기온은 {temp}도입니다. 하늘은 {sky}입니다.'
    elif '환율' in input_txt:
        answer_txt = '금일 원 달러 환율은 1250원입니다.'
    elif '추천' in input_txt:
        answer_txt = '오늘은 파랑색이 들어간 의상이 좋을 것 같아요. 화면에서 선택해보시죠.'
    elif '고마워' in input_txt:
        answer_txt = '저도요. 이제 꺼지세요.'
    elif '종료' in input_txt:
        answer_txt = '좋은 하루 되세요.'
        speak(answer_txt)                   # 마지말 한 마디
        stop_listening(wait_for_stop=False) # 그만 듣기
        program_status = False              # 프로그램 종료
        # sys.exit()                        # 시스템까지 종료
    else:
        answer_txt = '다시 한 번 말씀해주시겠어요?'

    speak(answer_txt)

# TTS 
def speak(txt):
    print('[인공지능] '+txt)
    file_name = 'chat_bot/x_tts/voice.mp3'
    tts = gTTS(text = txt, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    # voice.mp3 삭제
    if os.path.exists(file_name):
        os.remove(file_name)

recog = sr.Recognizer()
mic = sr.Microphone()

speak('안녕하세요? 무엇을 도와드릴까요?')
# mic로 듣다가 뭔가 입력되면 listen 실행
stop_listening = recog.listen_in_background(mic, listen) 
# recog.listen_in_background() 함수는 백그라운드에서 오디오를 듣기 시작하고, 듣기를 중지하는 데 사용되는 객체를 반환함. 이 객체는 백그라운드 리스닝을 제어하기 위한 메서드를 가지고 있음.

# # 더 이상 듣지 않게 하기
# stop_listening(wait_for_stop=False)

# 프로그램 종료 안 되고 계속 대기하게 만들기, '종료' 명령 시 종료
while program_status:
    time.sleep(0.1) #0.1초 간격
