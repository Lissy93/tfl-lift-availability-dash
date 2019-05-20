#USAGE
#python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from pyimagesearch.centroidtracker import CentroidTracker
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import logging

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.6,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize our centroid tracker and frame dimensions
ct = CentroidTracker()
(H, W) = (None, None)

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
import csv

output = csv.writer(open('export_log_1.csv', 'w'))
output.writerow(['personID', 'status','time'])

# loop over the frames from the video stream
while True:
	# read the next frame from the video stream and resize it
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# if the frame dimensions are None, grab them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# construct a blob from the frame, pass it through the network,
	# obtain our output predictions, and initialize the list of
	# bounding box rectangles
	blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H),
		(104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()
	rects = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# filter out weak detections by ensuring the predicted
		# probability is greater than a minimum threshold
		if detections[0, 0, i, 2] > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for
			# the object, then update the bounding box rectangles list
			box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
			rects.append(box.astype("int"))

			# draw a bounding box surrounding the object so we can
			# visualize it
			(startX, startY, endX, endY) = box.astype("int")
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 255, 0), 2)

	# update our centroid tracker using the computed set of bounding
	# box rectangles
	objects = ct.update(rects)
	total_objects = 0
	tracking = {}
	seen_objects = []
	live_objects =[]
	# loop over the tracked objects
	current_objects = [x[0] for x in objects.items()]
	for 
	for (objectID, centroid) in objects.items():
		# draw both the ID of the object and the centroid of the
		# object on the output frame
		
		total_objects = total_objects + 1
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

		cv2.putText(frame, f"people: {total_objects}", (0,30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		
		if objectID not in seen_objects:
				seen_objects.append(objectID)
				live_objects.append(objectID)
				output.writerow([f"ID {objectID}", 'entered', time.time()])
		for objectID in live_objects:
    			if objectID not in current_objects:
    					live_objects.pop(objectID)
    					output.writerow([f"ID {objectID}", 'left', time.time()])
		
		print(f"current objects: {current_objects}")
		print(f"seen objects: {seen_objects}")
		print(f"live objects: {live_objects}")
		
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
logs = pd.DataFrame(tracking)
logs.to_csv(f"logs_{time.time}.csv")
cv2.destroyAllWindows()
vs.stop()