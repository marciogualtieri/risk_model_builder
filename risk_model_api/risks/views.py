from risks.models import Risk
from rest_framework import viewsets, permissions
from risks.serializers import RiskSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer