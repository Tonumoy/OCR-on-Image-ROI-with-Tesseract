# OCR-on-Image-ROI-with-Tesseract
Applying OCR on manually selected Region of Interests (using mouse drag) for Text extraction from Images

# Steps

1. Install pytesseract() and setting it to the path variable
    •	Tesseract Download Link: https://github.com/UB-Mannheim/tesseract/wiki
2. Importing the required libraries 
3. Reading the image file into python using OpenCV’s imread() method
4. Resizing the images and converting them into grey scale using OpenCV’s resize () and cvtColor() methods respectively 
5. Extracting the Region of Interest from the image manually using mouse drag. 
    •	For that, first we set an event listener to the mouse, enabling the user to select the region of interest. Here, we set two conditions, one being the left mouse button down       and second being the left mouse button up.
    •	We store the starting coordinates when the left mouse button is pressed and the ending coordinates when the left mouse button is released. 
    •	Then we extract the region between these starting and ending coordinates when ‘enter’ is pressed. If ‘c’ is pressed the coordinates are cleared.
6. Now, applying Optical Character Recognition (OCR) on the ROI using pytesseract. (Instead of Tesseract engine, Google Vision or Azure Vision could also be used).
