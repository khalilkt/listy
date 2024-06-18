from ..models.entities import *
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class WilayaList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WilayaSerializer
    filterset_fields = [] 
    search_fields = ["name", "name_ar"]
    ordering_fileds = []
    ordering = ['name']
    pagination_class = None


    def get_queryset(self):
        return Wilaya.objects.all()
    



class MoughataaList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MoughataaSerializer
    filterset_fields = ["wilaya"] 
    search_fields = ["name", "name_ar"]
    ordering_fileds = []
    ordering = ['name']
    pagination_class = None


    def get_queryset(self):
        return Moughataa.objects.all()

class CommuneList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommuneSerializer
    filterset_fields = ["moughataa"] 
    search_fields = ["name", "name_ar"]
    ordering_fileds = []
    ordering = ['name']
    pagination_class = None


    def get_queryset(self):
        return Commune.objects.all()

class CentreList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CentreSerializer
    filterset_fields = ["commune"] 
    search_fields = ["name", "name_ar"]
    ordering_fileds = []
    ordering = ['name']
    pagination_class = None


    def get_queryset(self):
        return Centre.objects.all()

class BureauList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BureauSerializer
    filterset_fields = ["centre"] 
    search_fields = ["name", "name_ar"]
    ordering_fileds = []
    ordering = ['name']
    pagination_class = None

    def get_queryset(self):
        return Bureau.objects.all()

class WilayaDetail(RetrieveAPIView):
    serializer_class = WilayaSerializer
    queryset = Wilaya.objects.all()

class MoughataaDetail(RetrieveAPIView):
    serializer_class = MoughataaSerializer
    queryset = Moughataa.objects.all()

class CommuneDetail(RetrieveAPIView):
    serializer_class = CommuneSerializer
    queryset = Commune.objects.all()

class CentreDetail(RetrieveAPIView):
    serializer_class = CentreSerializer
    queryset = Centre.objects.all()

class BureauDetail(RetrieveAPIView):
    serializer_class = BureauSerializer
    queryset = Bureau.objects.all()
    