import cv2, time
from datetime  import datetime
import argparse
import os
import pywhatkit

face_casacde=cv2.CascadeClassifier("C:\\Users\\mudit\\Downloads\\haarcascade_frontalface_default.xml")

print("Welcome To CVM Smart Security System")

video = cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    if frame is not None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_casacde.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
        for x,y,w,h in faces:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            exact_time=datetime.now().strftime('%Y-%b-%d-%H-%S-%f')
            cv2.imwrite("face detected "+exact_time+".jpg",img)




        cv2.imshow("Home Security System",frame)
        key=cv2.waitKey(1)

        if key==ord('q'):
            print("Saving and Uploading data....")
            ap=argparse.ArgumentParser()
            ap.add_argument("-ext","--extension",required=False,default='jpg')
            ap.add_argument("-o","--output",required=False,default='output.mp4')
            args=vars(ap.parse_args())


            dir_path='.'
            ext=args['extension']
            output=args['output']


            images=[]

            for f in os.listdir(dir_path):
                if f.endswith(ext):
                    images.append(f)



            image_path=os.path.join(dir_path,images[0])
            frame=cv2.imread(image_path)
            height,width,channels=frame.shape

            forcc=cv2.VideoWriter_fourcc(*'mp4v')
            out=cv2.VideoWriter(output,forcc,5.0,(width,height))


            for image in images:
                image_path=os.path.join(dir_path,image)
                frame=cv2.imread(image_path)
                out.write(frame)

            break



print("Data Successfully saved...")

print("Warning !...someone entered in your room !!!...be careful !")
print("The exact date and time when the Intruder entered in the room ",exact_time)
pywhatkit.sendwhatmsg_instantly("xxxxxxxxxx","Warning !!!...someone is in your room !...be careful !!!",10, True, 5)   # In the place of xxxxxxxxx type the phone number on which you want alert message on whatsapp!!
pywhatkit.sendwhatmsg_instantly("xxxxxxxxxx","Warning !!!...someone is in your room !...be careful !!!",10, True, 5)
pywhatkit.sendwhatmsg_instantly("xxxxxxxxxx","Warning !!!...someone is in your room !...be careful !!!",10, True, 5)
pywhatkit.sendwhatmsg_instantly("xxxxxxxxxx","Warning !!!...someone is in your room !...be careful !!!",10, True, 5)



video.release()
cv2.destroyAllWindows
