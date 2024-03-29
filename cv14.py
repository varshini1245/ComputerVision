import cv2
import numpy as np
input_video_path = 'input_video.mp4'
cap = cv2.VideoCapture(input_video_path)
src_points = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
dst_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (width, height))
        out.write(transformed_frame)

        cv2.imshow('Transformed Frame', transformed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
