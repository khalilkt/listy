from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vote.models.person import PersonSerializer, Person, UserPerson, UserPersonSerializer
from rest_framework.permissions import IsAuthenticated
from ..models.entities import *
from rest_framework.response import Response
from utils import create_random_data
from django.db.models import Exists, OuterRef

class PersonList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonSerializer
    filterset_fields = [] 
    search_fields = ["name", "name_ar", "birth_place", "birth_place_ar"]
    ordering_fileds = []
    ordering = ['name']

    def get_queryset(self):
        ret = Person.objects.def_queryset()
        user = self.request.user
        user_person_subquery = UserPerson.objects.filter(
        user=user,
        person=OuterRef('pk')
        )
        ret = ret.annotate(user_person_id = user_person_subquery.values('id'))
        return ret

class MyPersonList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPersonSerializer
    filterset_fields = [] 
    search_fields = []
    ordering_fileds = []
    ordering = ['person__name']

    def get(self, request, *args, **kwargs):
        # create_random_data(Wilaya, 20)
        # create_random_data(Moughataa, 20)
        # create_random_data(Commune, 20)
        # create_random_data(Centre, 20)
        # create_random_data(Bureau, 20)
        # create_random_data(Person, 10000)
        # return Response("ok")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        request.data['user'] = user.id
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        user  = self.request.user
        ret = UserPerson.objects.filter(user=user)
        return ret
        
class MyPersonDetail(RetrieveUpdateDestroyAPIView   ):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPersonSerializer
    queryset = UserPerson.objects.all()

    def get_queryset(self):
        user  = self.request.user
        ret = UserPerson.objects.filter(user=user)
        return ret