#This a Python App that allows someone to save a screenshot and have the texted extracted from it. 

# This activates the Optical Character Recognition Utility, it must be installed via PIP. 
import easyocr

# file name in between "" below. 
image = "capture.png"

# This tells the OCR it will be reading English
reader = easyocr.Reader(['en'])

#This tells the OCR to look for text in the image named above in image = "capture.png" 
result = reader.readtext(image)

# This formats the text from the image into a much more readble format
for (bbox, text, prob) in result:
    print(text)

# The CUDA error is fine, most Office PC's do not have a nice GPU. 
# The result will be spit out under the CUDA error. 