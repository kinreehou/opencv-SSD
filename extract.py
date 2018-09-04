import cv2
vidcap = cv2.VideoCapture('Check-in.avi')
success,image = vidcap.read()
count = 0
while success and count<100:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1