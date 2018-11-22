    
    import cv2
    import numpy as np
    p=r'F:\Face Recog\haarcascade_frontalface_default.xml'
    print(p)
    detector = cv2.CascadeClassifier(p)
    cam=cv2.VideoCapture(0);
    while(True):
        ret, img = cam.read();  
        faces = detector.detectMultiScale(img, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyALLWindowns()
    
