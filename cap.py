import cv2
import datetime
def num(x):
    '''用来按顺序命名'''
    x = x +1
    return x
def video(u):
    f = cv2.VideoWriter_fourcc(*'MP42')
    cam_url1 = 'rtsp://admin:123456@192.168.123.10:554/Streaming/Channels/201'
    cam_url2 = 'rtsp://admin:123456@192.168.123.20:554/Streaming/Channels/201'
    cam_url3 = 'rtsp://admin:123456@192.168.123.30:554/Streaming/Channels/201'
    u=num(u)
    cap1 = cv2.VideoCapture(cam_url1)
    cap2 = cv2.VideoCapture(cam_url2)
    cap3 = cv2.VideoCapture(cam_url3)
    out1 = cv2.VideoWriter("cam01#" + str(u) + ".avi", f, 20, (1920, 1080))
    out2 = cv2.VideoWriter("cam02#" + str(u) + ".avi", f, 20, (1920, 1080))
    out3 = cv2.VideoWriter("cam03#" + str(u) + ".avi", f, 20, (1920, 1080))
    # 为保存视频做准备
    want_time=datetime.datetime.now()+datetime.timedelta(seconds=20) #设置每一段想录多长时间
    want_time_hour=want_time.hour
    want_time_minute=want_time.minute
    want_time_second=want_time.second


    while True:
        # 一帧一帧的获取图像
        time_now_hour=datetime.datetime.now().hour
        time_now_minute=datetime.datetime.now().minute
        time_now_second=datetime.datetime.now().second
        ret1,frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        ret3, frame3 = cap3.read()
        frame1 = cv2.flip(frame1, 1)
        frame2 = cv2.flip(frame2, 1)
        frame3 = cv2.flip(frame3, 1)

        out1.write(frame1)
        out2.write(frame2)
        out3.write(frame3)

        # 显示结果帧
        cv2.imshow("cam1", frame1)
        cv2.imshow("cam2", frame2)
        cv2.imshow("cam3", frame3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time_now_hour==want_time_hour and time_now_minute == want_time_minute and time_now_second ==want_time_second:
            video(u)
    # 释放摄像头资源
    cap1.release()
    cap2.release()
    cap3.release()

    out1.release()
    out2.release()
    out3.release()

    cv2.destroyAllWindows()
if __name__ == '__main__':
    video(0)
