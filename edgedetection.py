import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
  ret, frame = cap.read()
  cv2.imshow('The_input_frame', frame)
  edges = cv2.Canny(frame,100,100)
  cv2.imshow('Edges',edges)
  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break
cap.release()
