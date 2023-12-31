import os, sys
import cv2
from source.exception import FaceDetectionException
from source.logger import logging

class FaceDetectionWebcam:

    def load_camera(self):
        try:
            # Create a CascadeClassifier Object
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            video_capture = cv2.VideoCapture(0) # for defult camera 1 for your othe camera

            while True:
                # Capture frame-by-frame
                ret, frame = video_capture.read()

                # Reading image as gray scale image
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Search the coordinates of the image
                faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )

                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display the resulting frame
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # When everything is done, release the capture
            video_capture.release()
            cv2.destroyAllWindows()

        except Exception as e:
            raise FaceDetectionException(e,sys)