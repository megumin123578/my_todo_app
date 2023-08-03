import streamlit as st
import cv2 as cv
camera_image = st.camera_input('Camera')
print(camera_image)

img = cv.imread(camera_image[name])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
