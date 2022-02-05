# Face Recognition
THIS IS AN EXTENSION TO MY PERSONAL PROJECT CALLED P.A.V


# Installation 


## Download and install an application called "IP Webcam"

> Link: https://bit.ly/ip_webcam_app
> 
> Connect both devices on same network, and start the server in the app on android phone.

## If you wish to use webcam, remove the following code snippet from **main.py** and uncomment the code at line

- Line 8 - 17
```sh
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
```
- Line 37 -38
 ```sh
 driver.find_element_by_id('flashbtn').click()                                 
 driver.quit() 
 ```
 - Line 81
 ```sh
 driver.find_element_by_id('flashbtn').click()
 ```
 
 ## And uncomment the code.
 - Line 4
 ```sh
 cap = cv2.VideoCapture(0)
 ```
 
 ## Click a picture of yourself and paste in the *./faces* folder. 
 > The picture should in *.jpg* format.
 > Rename it to your name.
