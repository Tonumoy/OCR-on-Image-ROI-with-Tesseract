# OCR-on-Image-ROI-with-Tesseract
Applying OCR on manually selected Region of Interests (using mouse drag) for Text extraction from Images

# Steps

1. Install pytesseract() and setting it to the path variable
    -•	Tesseract Download Link: https://github.com/UB-Mannheim/tesseract/wiki
2. Import the required libraries 
3. Read the image file into python using OpenCV’s imread() method
4. Resize (if necessary) the images and converting them into grey scale using OpenCV’s resize () and cvtColor() methods respectively 
5. Extract the Region of Interest from the image manually using mouse drag. 
    -•	Starting coordinates are stored when the left mouse button is pressed and the ending coordinates when the left mouse button is released. 
    -•	Extract the region between these starting and ending coordinates when ‘enter’ is pressed. If ‘c’ is pressed the coordinates are cleared.
6. Optical Character Recognition (OCR) is then applied on the ROI using pytesseract. (Instead of Tesseract engine, Google Vision or Azure Vision could also be used).
