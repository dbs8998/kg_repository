# https://www.youtube.com/watch?v=fyJB1t0o0ms 
# load models
# load video (도로 상황 비디오)
# read frames
# detect vehicles
# track vehicles
# detect license plates
# assign license plate to car
# crop license plate
# process license plate
# read license plate number
# return results

from ultralytics import YOLO

# YOLO 기본 / 차번호 감지 학습모델
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO()