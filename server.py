

import random
import time
import socket
import io
import os
import cv2
import math
import select
import fcntl, os
import errno
from multiprocessing.pool import ThreadPool
import threading

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


TCP_IP = '127.0.0.1'
TCP_PORT = 13004
BUFFER_SIZE = 20
#GOOGLE_APPLICATION_CREDENTIALS="/Users/kcpoduru/Desktop/hackathon/weatherapp-1bd8212d7286.json"
def googlevisionapi(location,keyword):
	client = vision.ImageAnnotatorClient()
        print("inside google " + keyword)
		#The name of the image file to annotate
	file_name = os.path.join(
		    os.path.dirname(__file__),
		    'images/slice'+str(location)+'.jpg')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
		image = types.Image(content=content)

	# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		for label in labels:
			print(label.description)
			if(label.description==keyword):
				return True, location
		return False, location


def Doprocess(value):
	img = cv2.imread('images/stream.jpg');
	height, width, channels = img.shape;
	location = 0;
	results = [];
	avg = 0;
	count = 0;
	keyword = value;
	print(height,width);
	for x in range(0,width,320):
		crop_img = img[0:height, x:x+320]
		cv2.imwrite('images/slice'+str(location)+'.jpg',crop_img)
		results.append(pool.apply_async(googlevisionapi, (location,value)))
		location+=1;

	results = [r.get() for r in results]
	print(results)
	for v in results:
		print(v)
		if(v[0]==True):
			avg = avg + v[1];
			count+=1;
	if count == 0:
		return "not found"
	return math.floor(avg/count)




video_capture = cv2.VideoCapture(0)
pool = ThreadPool(processes=8)
prevline = ""


while 1:

  f2 = open('file2.txt', 'r')
  dataMain = f2.readline()
  f2.close()
  f2 = open('file2.txt', 'w')
  f2.write("Null")
  f2.close()
  ret, frame = video_capture.read()
  cv2.imshow('Video', frame)
  cv2.waitKey(1)


  if(dataMain == "cup" or dataMain == "water" or dataMain == "face" or dataMain == "forehead" or dataMain == "bottle" or dataMain == "watch" or dataMain == "phone" or dataMain == "hand"):
        print(dataMain)
        print("entered")
	cv2.imwrite('images/stream.jpg',frame)
	print("done");
	position = Doprocess(dataMain);

        f = open('file.txt','w')
        if(position == 0.0):
	    print(position)
            f.write("-7.5")

        if(position == 1.0):
	    print(position)
            f.write("-2.5")

        if(position == 2.0):
	    print(position)
            f.write("2.5")

        if(position == 3.0):
	    print(position)
            f.write("7.5")

        if(position == "not found"):
	   print("not found")
           f.write("1")
        f.close()




pool = ThreadPool(processes=4)

video_capture.release()
cv2.destroyAllWindows()
