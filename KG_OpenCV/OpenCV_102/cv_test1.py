import cv2
import datetime
import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image

# --------------- 폴더 생성 ---------------
os.makedirs('Capture', exist_ok=True)

# --------------- 파라미터 설정 ---------------
FRAME_WIDTH, FRAME_HEIGHT = 640, 480
THRESHOLD = 40       # 움직임 감지 임계값
DIFF_MIN = 10        # 움직임 픽셀 개수 임계값
KEEP_RECORD_FRAMES = 50  # 움직임이 멈춘 후 유지할 프레임 수
FONT_PATH = 'fonts/SCDream6.otf'

# --------------- 카메라 초기화 ---------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# --------------- 폰트 로드 ---------------
try:
    font = ImageFont.truetype(FONT_PATH, 20)
except:
    font = None
    print(f"⚠️ 폰트를 찾을 수 없습니다: {FONT_PATH}")

# --------------- 움직임 비교 함수 ---------------
def get_diff_img(frame_a, frame_b, frame_c, threshold):
    gray_a = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    gray_c = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    diff_ab = cv2.absdiff(gray_a, gray_b)
    diff_bc = cv2.absdiff(gray_b, gray_c)

    _, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    _, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
    diff_count = cv2.countNonZero(diff)

    return diff, diff_count

# --------------- VideoWriter 상태 ---------------
video_writer = None
record_counter = 0

# --------------- 초기 프레임 읽기 ---------------
ret, frame_a = cap.read()
ret, frame_b = cap.read()

print("[INFO] CCTV 감지 시작")

try:
    while True:
        ret, frame_c = cap.read()
        if not ret:
            print("❌ 카메라 프레임 읽기 실패")
            break

        frame = frame_c.copy()
        t_now = datetime.datetime.now()
        t_str_overlay = t_now.strftime('%Y/%m/%d %H:%M:%S')
        t_str_filename = t_now.strftime('%Y_%m_%d_%H_%M_%S')

        # 움직임 감지
        diff, diff_count = get_diff_img(frame_a, frame_b, frame_c, THRESHOLD)

        if diff_count > DIFF_MIN:
            record_counter = KEEP_RECORD_FRAMES

        # ------------ 녹화 관리 ------------
        if record_counter > 0:
            if video_writer is None:
                # mp4v 코덱 사용 (.mp4)
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                filename = f"Capture/motion_{t_str_filename}.mp4"
                video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (FRAME_WIDTH, FRAME_HEIGHT))

                if video_writer.isOpened():
                    print(f"[녹화 시작] {filename}")
                else:
                    print(f"❌ VideoWriter 생성 실패: {filename}")
                    video_writer = None

            if video_writer and video_writer.isOpened():
                video_writer.write(frame_c)
                record_counter -= 1

                if record_counter == 0:
                    video_writer.release()
                    video_writer = None
                    print("[녹화 종료]")
        else:
            if video_writer:
                video_writer.release()
                video_writer = None
                print("[녹화 강제 종료]")

        # ------------ 화면 출력 ------------
        cv2.rectangle(frame, (10, 15), (340, 35), (0, 0, 0), -1)
        if font:
            pil_img = Image.fromarray(frame)
            draw = ImageDraw.Draw(pil_img)
            draw.text((10, 15), f"CCTV {t_str_overlay}", font=font, fill=(255,255,255))
            frame = np.array(pil_img)
        else:
            cv2.putText(frame, f"CCTV {t_str_overlay}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

        cv2.imshow("Original", frame)
        cv2.imshow("Motion Detection", diff)

        key = cv2.waitKey(30)
        if key == ord('q'):
            print("[종료 요청]")
            break

        # 프레임 업데이트
        frame_a = frame_b
        frame_b = frame_c

except KeyboardInterrupt:
    print("[중단 요청]")

finally:
    if video_writer:
        video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
    print("[자원 해제 완료]")
