from django.db import models
from rest_framework import serializers

class PersonManager(models.Manager):
    def def_queryset(self):
        ret =  super().get_queryset()
        ret = ret.annotate(centre = models.F('bureau__centre'), commune = models.F('bureau__centre__commune'), moughataa = models.F('bureau__centre__commune__moughataa'), wilaya = models.F('bureau__centre__commune__moughataa__wilaya'))
        return ret   
    

class Person(models.Model):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    birth_place = models.CharField(max_length=100)
    birth_place_ar = models.CharField(max_length=100, default="")
    order = models.IntegerField() 
    bureau = models.ForeignKey('Bureau', on_delete=models.CASCADE)

    objects = PersonManager()

class PersonSerializer(serializers.ModelSerializer):
    centre = serializers.IntegerField(read_only=True)
    commune = serializers.IntegerField(read_only=True)
    moughataa = serializers.IntegerField(read_only=True)
    wilaya = serializers.IntegerField(read_only=True)
    user_person_id = serializers.IntegerField(read_only=True)
    bureau_name = serializers.CharField(source='bureau.name', read_only=True)
    centre_name = serializers.CharField(source='bureau.centre.name', read_only=True)
    commune_name = serializers.CharField(source='bureau.centre.commune.name', read_only=True)
    moughataa_name = serializers.CharField(source='bureau.centre.commune.moughataa.name', read_only=True)
    wilaya_name = serializers.CharField(source='bureau.centre.commune.moughataa.wilaya.name', read_only=True)
    

    class Meta:
        model = Person
        fields = '__all__'

class UserPerson(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    nnn = models.CharField(max_length=15)
    phone = models.CharField(default="", max_length=100)
    note = models.TextField(default="")

    class Meta:
        unique_together = ['user', 'person']

class UserPersonSerializer(serializers.ModelSerializer):
    person_detail = serializers.SerializerMethodField()

    def get_person_detail(self, obj):
        person =  Person.objects.def_queryset().get(id=obj.person.id)
        return PersonSerializer(person).data
    class Meta:
        model = UserPerson
        read_only_fields = ['person_detail']
        fields = '__all__'

        