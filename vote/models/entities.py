import random
import string
from rest_framework import serializers
from django.db import models

class Wilaya(models.Model):
    name_ar = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'
    
class Moughataa(models.Model):
    name_ar = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class MoughataaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moughataa
        fields = '__all__'
    
class Commune(models.Model):
    name_ar = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'

class Centre(models.Model):
    name_ar = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centre
        fields = '__all__'

class Bureau(models.Model):
    name_ar = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class BureauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bureau
        fields = '__all__'
    