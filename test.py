from oauth2client.client import flow_from_clientsecrets
from google.cloud import vision
import io
import os
import requests, shutil

def download_image(url):
    filename = 'test.jpg'
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def detect_labels(url):
	vision_client = vision.Client()
	# image = client.image(filename='test.jpg')
	download_image(url)

	file_name = os.path.join(
	        os.path.dirname(__file__),
	        'test.jpg')


	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
		image = vision_client.image(content=content)

	    # Performs label detection on the image file
	labels = image.detect_labels()

	print('Labels:')
	slabels =[]
	for label in labels:
		slabels.append(label.description)

	faces = image.detect_faces()
	facelist = []

    for face in faces:
    	facelist.append(face.emotions.anger)
    	facelist.append(face.emotions.joy)
    	facelist.append(face.emotions.surprise)
        # print('anger: {}'.format(face.emotions.anger))
        # print('joy: {}'.format(face.emotions.joy))
        # print('surprise: {}'.format(face.emotions.surprise))

	return '\n'.join(slabels+facelist)


# def detect_labels_from_url(uri):
# 	"""Detects labels in the file located in Google Cloud Storage."""
# 	vision_client = vision.Client()
# 	image = vision_client.image(source_uri=uri)
# 	labels = image.detect_labels()
# 	print('Labels:')
# 	shots =[]
# 	for label in labels:
# 		shots.append(label)
# 	return shots
    
# print detect_labels()