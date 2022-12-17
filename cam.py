import cv2 as cv

cam = cv.VideoCapture(0)
i = 0
while True:
    ret,frame = cam.read()

    cv.imshow('Press Q to quit',frame)

    if cv.waitKey(1)==ord('c'):
        cv.imwrite('img'+str(i)+'.png',frame)
        i+=1
    if cv.waitKey(1)==ord('q'):
        # cv.imwrite('first.png',frame)
        break
cam.release()

