from oauth2client.client import flow_from_clientsecrets
from google.cloud import vision
import io
import unicodedata
import os
import requests, shutil


dd = {'VERY_UNLIKELY':'10%','VERY_LIKELY':'95%','LIKELY':'80%','POSSIBLE':'65%','UNKNOWN':'50%','UNLIKELY':'30%'}

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
    slabels =["\nLabels:"]
    for label in labels:
        slabels.append(label.description)


    # Performs Face detection on the image file

    faces = image.detect_faces()
    facelist = ["\nFaces:"]
    if not faces:
        facelist.append("Sorry!! No faces recognized")
    else:
        for face in faces:
            facelist.append("anger-"+dd[face.emotions.anger.value])
            facelist.append("joy-"+dd[face.emotions.joy.value])
            facelist.append("surprise-"+dd[face.emotions.surprise.value])
            facelist.append("sorrow-"+dd[face.emotions.sorrow.value])
            facelist.append("\n")

    # # Performs Text detection on the image file
    texts = image.detect_text()
    textlist = ["\nTexts:"]
    if not texts:
        textlist.append("Sorry!! No Text Found")
    else:
        for text in texts:
            textlist.append(text.description)
            break
        
    # textlist = textlist.encode('ascii','ignore')
    # print textlist


    # Performs Logo detection on the image file
    logos = image.detect_logos()

    logolist = ["\nLogos:"]
    if not logos:
        logolist.append("No Logos Found")
    else:
        for logo in logos:
            logolist.append(logo.description)

    # Performs Logo detection on the image file
    landmarks = image.detect_landmarks()
    landlist = ["\nLandmarks:"]
    if not landmarks:
        landlist.append("No Logos Found")
    else:
        for land in landmarks:
            landlist.append(land.description)


    return '\n'.join(facelist+logolist+slabels+textlist+landlist)

    

# def detect_labels_from_url(uri):
#   """Detects labels in the file located in Google Cloud Storage."""
#   vision_client = vision.Client()
#   image = vision_client.image(source_uri=uri)
#   labels = image.detect_labels()
#   print('Labels:')
#   shots =[]
#   for label in labels:
#       shots.append(label)
#   return shots
    
# print detect_labels()