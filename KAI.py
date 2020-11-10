import face_recognition
import cv2
import numpy as np
import os
import pytesseract
from threading import Thread
import shutil

video_capture = cv2.VideoCapture(0)

def face_rec():
    ## Load a sample picture and learn how to recognize it.
    kudos_image = face_recognition.load_image_file(r"C:\Users\CHIJINDU\Desktop\KudosPix\KUDOS-J.jpg")
    kudos_face_encoding = face_recognition.face_encodings(kudos_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [kudos_face_encoding]
    known_face_names = ["Sir Kudos"]
    i =0
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        #Get image clips and extract text form it
        if i%30 == 0:
            cv2.imwrite(r'C:\Users\CHIJINDU\Desktop\ml learn\{index}.jpg'.format(index=i), frame)
            file_cop(r'C:\Users\CHIJINDU\Desktop\ml learn', r'C:\Users\CHIJINDU\Desktop\KUDOSCOPY')
            thread = Thread(target= extract_text, args=())
            thread.start()

        i += 1

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def file_cop(src, dest):
    src_file = os.listdir(src)
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)

def extract_text():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #path for the folder for getting the raw images
    path = r'C:\Users\CHIJINDU\Desktop\ml learn'

    # iterating the images inside the folder
    for imageName in os.listdir(path):
        inputPath= os.path.join(path, imageName)
        img_cv = cv2.imread(inputPath)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

        #applying ocr using pytesseract for python
        text = pytesseract.image_to_string(img_rgb, lang='eng')
        print(text)

        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #   break


face_rec()
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#if len(os.listdir(r'C:\Users\CHIJINDU\Desktop\ml learn')) >2:
 #               shutil.copy2(r'C:\Users\CHIJINDU\Desktop\ml learn',
  #               r'C:\Users\CHIJINDU\Desktop\LORD OF THE RINGS')
