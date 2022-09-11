from tkinter import W
import cv2 
import time
cap = cv2.VideoCapture('test.mp4')
cap2 = cv2.VideoCapture('test.mp4')
cap3 = cv2.VideoCapture('test.mp4')


W = cv2.CAP_PROP_FRAME_WIDTH
H = cv2.CAP_PROP_FRAME_HEIGHT
fps = 25
codec = cv2.VideoWriter_fourcc(*'mp4v')
# codec = cv2.VideoWriter_fourcc(*'H264')
video = cv2.VideoWriter('test_single.mp4', codec, fps, (W, H))
video_multi = cv2.VideoWriter('test_multi.mp4', codec, fps, (W, H))
video_multi_non_GIL = cv2.VideoWriter('test_multi_nonGIL.mp4', codec, fps, (W, H))

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) +1


def writer(x):
        ret, img = cap2.read()
        img = cv2.putText(img,
                text=str(x).zfill(4),
                org=(100, 300),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,
                color=(0, 255, 0),
                thickness=2,
                lineType=cv2.LINE_4)
    
        video_multi.write(img)
def writer_non_GIL(x):
        ret, img = cap3.read()
        cv2.putText(img,
                text=str(x).zfill(4),
                org=(100, 300),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,
                color=(0, 255, 0),
                thickness=2,
                lineType=cv2.LINE_4)
    
        video_multi_non_GIL.write(img)


if __name__ == "__main__":
    start = time.time()
    for i in range(frame_count) :
        ret, img = cap.read()
    
        
        if ret == False:
            break
    
        cv2.putText(img,
                text=str(i).zfill(4),
                org=(100, 300),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,
                color=(0, 255, 0),
                thickness=2,
                lineType=cv2.LINE_4)
        video.write(img)
    cap.release()
    video.release()
    
    print(time.time() - start)
    
    from multiprocessing import Pool    
    
    start_multi = time.time()

    
    p = Pool(4)
    p.map(writer, range(frame_count))
    video_multi.release()
    
    print(time.time() - start_multi)
    from concurrent.futures import ProcessPoolExecutor

    start_multi_non_GIL = time.time()
    pool = ProcessPoolExecutor(max_workers=2)
    pool.map(writer_non_GIL, range(frame_count))
    video_multi_non_GIL.release()
    print(time.time() - start_multi_non_GIL)



