from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from .ser import FileSerializer,ImageSerializer
import numpy
import json
import cv2 
import pytesseract
from PIL import Image
from pytesseract import pytesseract ,Output
from .models import ImageFile,ImageKey
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from rest_framework import viewsets
import json

class ImageView(viewsets.ModelViewSet):
    queryset=ImageFile.objects.all()
    serializer_class=ImageSerializer   
  
    http_method_names = ['post',] 
    
    def create(self, request):
        obj=ImageKey.objects.filter(code=request.data['code']).count()
        if obj >=1:
          test=ImageFile()
          test.image=request.data['image']
          test.save()
          img=request.data['image']
          image = 'media/'+str(img)
          im = Image.open(image)
          test.text = pytesseract.image_to_data(im, output_type=Output.DICT)
          data=test.text
          test.save()
          return Response(data, status=status.HTTP_201_CREATED)
        else:
         return Response(data="You are not autherized...!", status=status.HTTP_404_NOT_FOUND)
    





            
    