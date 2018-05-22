import io
import os
import cv2
import math

from multiprocessing.pool import ThreadPool

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def googlevisionapi(location,keyword):
	client = vision.ImageAnnotatorClient()

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
			#print(label.description)
			if(label.description==keyword):
				return True, location
		return False, location


def Doprocess():
	img = cv2.imread('images/stream.jpg');
	height, width, channels = img.shape;
	location = 0;
	results = [];
	avg = 0;
	count = 0;
	keyword="cup"
	for x in range(0,width,160):
		crop_img = img[0:height, x:x+160]
		cv2.imwrite('images/slice'+str(location)+'.jpg',crop_img)
		results.append(pool.apply_async(googlevisionapi, (location,keyword)))
		location+=1;

	results = [r.get() for r in results]
	print(results)
	for v in results:
		print(v)
		if(v[0]==True):
			avg = avg + v[1];
			count+=1;
	return math.floor(avg/count)



video_capture = cv2.VideoCapture(0)
pool = ThreadPool(processes=4)
while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	# Display the resulting frame
	cv2.imshow('Video', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite('images/stream.jpg',frame)
		print("done");
		position = Doprocess();
		print(position)



	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

#Instantiates a client
