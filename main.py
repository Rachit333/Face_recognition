import face_recognition as fr, os, cv2, face_recognition,time, numpy as np, pyttsx3, netifaces
from time import sleep

#cap = cv2.VideoCapture(0)
# UNCOMMENT THE ABOVE CODE TO USE WEBCAM.

# -----------------------------------------------------------CONFIG FOR IP CAMERA--------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options;
driver_path = r"C:\Windows\chromedriver.exe"
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(driver_path, chrome_options=options)
ip = netifaces.gateways()['default'][netifaces.AF_INET][0]
driver.get(f"http://{ip}:8080/")
cap = cv2.VideoCapture(f"http://{ip}:8080/video")
#----------------------------------------------------------------------------------------------------------------------

# CONFIG FOR SPEACH
engine = pyttsx3.init(driverName='sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',100.0)
#

# CONFIG FOR FACE DETECTION
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#

def save_img(img):
    cv2.imwrite('resulting_pic.jpg',img)
    cv2.destroyAllWindows()
    driver.find_element_by_id('flashbtn').click()                                  ####
    driver.quit()                                                                  ####

def get_encoded_faces():
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    return encoded

def unknown_image_encoded(img):
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]
    return encoding

def classify_face(im):
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    img = cv2.imread(im, 1)
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    face_names = []
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    return face_names

while True:
    success, img = cap.read()
    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y),(x+w,y+h), (255, 0, 0), 2)
    if len(faces) != 0:
        driver.find_element_by_id('flashbtn').click()                               ####
        save_img(img)
        break
        
cap.release()
os.system("cls")
faces = classify_face("resulting_pic.jpg")
print(faces)

engine.say(f"hello{faces}")
engine.runAndWait()
