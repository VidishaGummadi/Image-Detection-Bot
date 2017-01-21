from oauth2client.client import flow_from_clientsecrets
from google.cloud import vision
import io
import os

def detect_labels():
	vision_client = vision.Client()
	# image = client.image(filename='test.jpg')

	file_name = os.path.join(
	        os.path.dirname(__file__),
	        'test.jpg')


	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
		image = vision_client.image(content=content)

	    # Performs label detection on the image file
	labels = image.detect_labels()

	print('Labels:')
	shots =[]
	for label in labels:
		shots.append(label.description)
	return shots


def detect_labels_from_url(uri):
	"""Detects labels in the file located in Google Cloud Storage."""
	vision_client = vision.Client()
	image = vision_client.image(source_uri=uri)
	labels = image.detect_labels()
	print('Labels:')
	shots =[]
	for label in labels:
		shots.append(label)
	return shots
    
print detect_labels()