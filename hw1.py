import cv2 as cv
import sys

img = cv.imread('./soccer.webp')

if img is None:
  sys.exit('파일을 찾을 수 없습니다.')
  
BrushSize = 10
LColor, RColor = (225, 0, 0), (0, 0, 255)

def painting(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDOWN:
    cv.circle(img, (x, y), BrushSize, LColor, -1)
  elif event == cv.EVENT_RBUTTONDOWN:
    cv.circle(img, (x, y), BrushSize, RColor, -1)
  elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
    cv.circle(img, (x, y), BrushSize, LColor, -1)
  elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
    cv.circle(img, (x, y), BrushSize, RColor, -1)
  
  cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)

cv.setMouseCallback('Painting', painting)

while(True):
  key = cv.waitKey(1)
  if key == ord('q'):
    cv.destroyAllWindows()
    break
  elif key == ord('+') and BrushSize < 50:
    BrushSize += 1
  elif key == ord('-') and BrushSize > 1 :
    BrushSize -= 1
  