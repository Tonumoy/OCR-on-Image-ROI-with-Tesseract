# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:49:30 2021

@author: Tonumoy
"""



# NOTE TO USER/READER:
# 1) This module is developed and tested using Python 3.6 and above and the author 
#    recommends the same for better and smooth execution.
# 2) pytesseract has to be installed seperately
# 2) Import necessary libraries : pandas,OpenCV, pytesseract
# 3) Ensure the necessary environment variables are set correctly (especially for pyteserract).
# 3) For demonstration purposes, the user/reader is adviced to mention the location of the input image
#    in the IMAGE_FILE_LOCATION variable before executing.


import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'Location of tesseract.exe file' #note the location while installing tesseract


IMAGE_FILE_LOCATION =  r"Image File Location"
input_img = cv2.imread(IMAGE_FILE_LOCATION) # image read
input_img = cv2.resize(input_img,(1500,800)) # resizing image
#img_gray =  cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY) # convert image to grayscale if needed


#################################################################################################
# REGION OF INTEREST (ROI) SELECTION

    # initializing the list for storing the coordinates 
coordinates = [] 
  
# Defining the event listener (callback function)
def shape_selection(event, x, y, flags, param): 
    # making coordinates global
    global coordinates 
  
    # Storing the (x1,y1) coordinates when left mouse button is pressed  
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
  
    # Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
  
        # Drawing a rectangle around the region of interest (roi)
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,255,255), 2) 
        cv2.imshow("image", image) 
  
  
# load the image, clone it, and setup the mouse callback function 
image = input_img #img_gray
image_copy = image.copy()
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 
  
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    if key==13: # If 'enter' is pressed, apply OCR
        break
    
    if key == ord("c"): # Clear the selection when 'c' is pressed 
        image = image_copy.copy() 
  
if len(coordinates) == 2: 
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                               coordinates[0][0]:coordinates[1][0]] 
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_roi) 
    cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows()  
    

#####################################################################################################
# OPTICAL CHARACTER RECOGNITION (OCR) ON ROI

text = pytesseract.image_to_string(image_roi)
print("The text in the selected region is as follows:")
print(text)

#####################################################################################################
# SAVING THE TEXT CORRESPONDING TO THE IMAGE INTO A .txt FILE
with open("Output.txt", "w") as text_file:
    text_file.write(text)       
