from oauth2client.client import flow_from_clientsecrets
from google.cloud import vision
import io
import os
import requests, shutil
import unicodedata

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
	print slabels

	faces = image.detect_faces()
	facelist = ["\nFaces:"]
	if not faces:
		facelist.append("Sorry!! No faces recognized")
		print facelist
	else:		
		for face in faces:
			facelist.append("anger-"+face.emotions.anger.value)
			facelist.append("joy-"+face.emotions.joy.value)
			facelist.append("surprise-"+face.emotions.surprise.value)
			facelist.append("sorrow-"+face.emotions.sorrow.value)
			print('anger: {}'.format(face.emotions.anger))
			print('joy: {}'.format(face.emotions.joy))
			print('surprise: {}'.format(face.emotions.surprise))
			print('sorrow: {}'.format(face.emotions.sorrow))
			print facelist

	texts = image.detect_text()
	textlist = ["\nTexts:"]
	if not texts:
		textlist.append("Sorry!! No Text Found")
	else:
		for text in texts:
			textlist.append(text.description)
		textlist = " ".join(textlist[1])
	textlist = textlist.encode('ascii','ignore')
	print textlist

	# print '\n'.join(slabels+facelist)+textlist




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
url = "https://s-media-cache-ak0.pinimg.com/originals/b9/ab/e1/b9abe1a9b905ba8f6e19a6e20a836289.png"
detect_labels(url)