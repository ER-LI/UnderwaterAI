import cv2
import datetime
cam_url1='rtsp://admin:123456@192.168.123.10:554/Streaming/Channels/201'
cam_url2='rtsp://admin:123456@192.168.123.20:554/Streaming/Channels/201'
cam_url3='rtsp://admin:123456@192.168.123.30:554/Streaming/Channels/201'
f = cv2.VideoWriter_fourcc(*'MP42')
out1 = cv2.VideoWriter("test01.avi",f,10,(1920,1080))
out2 = cv2.VideoWriter("test02.avi",f,10,(1920,1080))
out3 = cv2.VideoWriter("test03.avi",f,10,(1920,1080))
cap1=cv2.VideoCapture(cam_url1)
cap2=cv2.VideoCapture(cam_url2)
cap3=cv2.VideoCapture(cam_url3) 

if cap1.isOpened():
    rval1, frame1 = cap1.read()  
else:
    cap1.open(cam_url1)
    rval1 = False
    print("error")
if cap2.isOpened():
    rval2, frame2 = cap2.read()
    
else:
    cap2.open(cam_url2)
    rval2 = False
    print("error")
if cap3.isOpened():
    rval3, frame3 = cap3.read()
    
else:
    cap3.open(cam_url3)
    rval3 = False
    print("error")
while rval1 or rval2 or rval3:
    frame1 = cv2.resize(frame1,(1920,1080))
    frame2 = cv2.resize(frame2, (1920, 1080))
    frame3 = cv2.resize(frame3, (1920, 1080))
    rval1, frame1 = cap1.read()
    rval2, frame2 = cap2.read()
    rval3, frame3 = cap3.read()
    if rval1 or rval2 or rval3 == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        #text = "1920x1080"
        time = str(datetime.datetime.now())
        #frame1 = cv2.putText(frame1,text,(10,50),font,0.5,(0,255,255),2,cv2.LINE_AA)
        frame1 = cv2.putText(frame1,time,(10,100),font,1,(0,255,255),2,cv2.LINE_AA)
        #frame2 = cv2.putText(frame2,text,(10,50),font,0.5,(0,255,255),2,cv2.LINE_AA)
        frame2 = cv2.putText(frame2,time,(10,100),font,1,(0,255,255),2,cv2.LINE_AA)
        frame3 = cv2.putText(frame3,time,(10,100),font,1,(0,255,255),2,cv2.LINE_AA)
        out1.write(frame1)
        cv2.imshow("cam_num1", frame1)
        out2.write(frame2)
        cv2.imshow("cam_num2", frame2)
        out3.write(frame3)
        cv2.imshow("cam_num3", frame3)
       
    else:
        break                                   
    key = cv2.waitKey(1)
    if key == 27:                                     
        break
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()                               
