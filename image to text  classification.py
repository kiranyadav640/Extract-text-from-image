
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from PIL import Image
import argparse
import cv2
import os


# In[2]:


#from pytesseract import image_to_string


# In[3]:


import pytesseract as tess


# In[4]:


img = cv2.imread("401.png",0)


# In[5]:


#Write the grayscale image to disk as a temporary file
filename = "{}.png".format(os.getpid())
print(filename)

cv2.imwrite(filename, img)


# In[6]:


# Load the image using PIL (Python Imaging Library), Apply OCR, and then delete the temporary file
text = tess.image_to_string(Image.open(filename))
print(text)
os.remove(filename)

