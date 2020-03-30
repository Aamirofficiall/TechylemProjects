from rest_framework import serializers
from .models import ImageFile,ImageKey


class ImageSerializer(serializers.ModelSerializer):

    code=serializers.CharField(max_length=255,required=False,allow_null=True)
    class Meta:
        model = ImageFile
        fields = ['id','text','image','code']


class FileSerializer(serializers.Serializer):
    text=serializers.CharField(max_length=255)
    code=serializers.CharField(max_length=255,required=False,allow_null=True)
    
    def create(self, validated_data):
        return ImageFile(text=self.validated_data['text'])