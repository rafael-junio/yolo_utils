"""Glare Removal (at least I tried)"""
import cv2

bgr = cv2.imread('test2.jpg')
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(16, 16))

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)
bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imwrite('test_result.jpg', bgr)