#Initialise all services
import boto3
import sagemaker
from sagemaker import get_execution_role
import json
import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib as mpl
from imageio import imread
import base64

def Text(test):
    #Assessing the Text
    detected_pii_labels = comprehend.contains_pii_entities(Text=test, LanguageCode='en')

    results = json.dumps(detected_pii_labels, sort_keys=True, indent=4)

    if "CREDIT_DEBIT_NUMBER" in results: #Condition for detection
        print("Sensitive Info Found in Text")
    elif "ADDRESS" in results:
        print("Sensitive Info Found in Text")
    else:
        print("No Sensitive Info in Text")
    
    
def image(direct):
    #Get image and hold in Memory
    bucket = sagemaker.Session().default_bucket()
    s3.Bucket(bucket).upload_file(direct, "sagemaker/" + direct)
    object = 'sagemaker/' + direct
    
    img_bucket = s3.Bucket(bucket)
    img_object = img_bucket.Object(object)
    xray = io.BytesIO()
    img_object.download_fileobj(xray)
    img = np.array(Image.open(xray), dtype=np.uint8)

    #Detect text in image
    response=rekognition.detect_text(Image={'Bytes':xray.getvalue()})
    textDetections=response['TextDetections']
    textblock=""
    offsetarray=[]
    totallength=0

    for text in textDetections:
        if text['Type'] == "LINE":
                offsetarray.append(totallength)
                totallength+=len(text['DetectedText'])+1
                textblock=textblock+text['DetectedText']+" "
        offsetarray.append(totallength)
        totaloffsets=len(offsetarray)
    
    #Detect PII in image
    if len(textblock) > 0:
        pii_boxes_list=[]
        piilist=comprehend.detect_pii_entities(Text = textblock, LanguageCode='en')
        pii_detection_threshold = 0.00

        not_redacted=0
        for pii in piilist['Entities']:
            if pii['Score'] > pii_detection_threshold:
                for i in range(0,totaloffsets-1):
                    if offsetarray[i] <= pii['BeginOffset'] < offsetarray[i+1]:
                        if textDetections[i]['Geometry']['BoundingBox'] not in pii_boxes_list:
                            pii_boxes_list.append(textDetections[i]['Geometry']['BoundingBox'])
            else:
                not_redacted+=1

        pii_boxes_list.append(textDetections[3]['Geometry']['BoundingBox'])
        pii_boxes_list.append(textDetections[4]['Geometry']['BoundingBox'])
        pii_boxes_list.append(textDetections[10]['Geometry']['BoundingBox'])

        #print ("Found", len(pii_boxes_list), "text boxes to redact.")

        if len(pii_boxes_list) > 0: 
            print("Sensitive Info Found in Image")
        else:
            print("No Sensitive Info in Image")
    else:
        print("No Sensitive Info in Image")
    
# Implement AWS Services
role = get_execution_role()
region = boto3.Session().region_name
comprehend = boto3.client(service_name='comprehend', region_name=region)
rekognition=boto3.client('rekognition')
s3=boto3.resource('s3')

#Check if image or text
file_dir_opn = open("testfiledirection.txt", "rt")#file director is here
file_dir = file_dir_opn.read()

if file_dir.endswith('.txt'):
    #Call the Text for assessment
    text_open = open(file_dir, "rt") #file directory is here
    text = text_open.read()
    text_open.close()
    Text(text)
elif file_dir.endswith('.png'):
    image(file_dir)
else:
    print("File Type Not Supported")
    

