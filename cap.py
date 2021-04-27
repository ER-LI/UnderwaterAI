import cv2
import datetime
cam_url1='rtsp://admin:123456@192.168.1.10:554/Streaming/Channels/201'
cam_url2='rtsp://admin:123456@192.168.1.20:554/Streaming/Channels/201'
cam_url3='rtsp://admin:123456@192.168.1.10:554/Streaming/Channels/201'
f = cv2.VideoWriter_fourcc(*'MP42')
out1 = cv2.VideoWriter("test01.avi",f,10,(1920,1080))
out2 = cv2.VideoWriter("test02.avi",f,10,(1920,1080))
#out3 = cv2.VideoWriter("test03.avi",f,10,(1920,1080))
cap1=cv2.VideoCapture(cam_url1)
cap2=cv2.VideoCapture(cam_url2)
#cap3=cv2.VideoCapture(cam_url3) #调用IP摄像头

if cap1.isOpened():
    rval, frame1 = cap1.read()
    rval, frame2 = cap2.read()#读取视频流
else:
    cap1.open(cam_url1)
    cap2.open(cam_url2)
    #cap.open(cam_url3) #打开读取的视频流
    rval = False
    print("error")
while rval:
    frame1 = cv2.resize(frame1,(1920,1080))
    rval, frame1 = cap1.read()
    frame2 = cv2.resize(frame2, (1920, 1080))
    rval, frame2 = cap2.read()
    #frame3 = cv2.resize(frame3, (1920, 1080))
    #rval, frame3 = cap3.read()
    if rval == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        #text = "1920x1080"
        #time = str(datetime.datetime.now())
        #frame = cv2.putText(frame,text,(10,50),font,0.5,(0,255,255),2,cv2.LINE_AA)
        #frame = cv2.putText(frame,time,(10,100),font,1,(0,255,255),2,cv2.LINE_AA)

        out1.write(frame1)
        out1.write(frame2)
       # out1.write(frame3)

        cv2.imshow("cam_num1", frame1)
        cv2.imshow("cam_num2", frame2)
       # cv2.imshow("cam_num3", frame3)# 显示视频流

    else:
        break
    key = cv2.waitKey(1)
    if key == 27:                                     #按ESC键退出
        break
cap1.release()
cap2.release()#释放摄像头
cv2.destroyAllWindows()                               #关闭窗口
