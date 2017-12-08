from risks.models import Risk
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from risks.serializers import RiskSerializer, FieldSerializer
import json
import jsonschema


with open('schemas/risk_schema.json', 'r') as schema_file:
    RISK_SCHEMA = schema_file.read()


#
# Django REST Framework doesn't support writable nested serializers at the moment:
# https://github.com/encode/django-rest-framework/issues/395
#
# TODO: Refactoring using built-in serializers after feature is implemented.
#
class RiskList(APIView):

    def __validate_data__(self, data):
        jsonschema.validate(
            data,
            json.loads(RISK_SCHEMA)
        )

    def __persist_risk__(self, risk_data):
        risk = Risk.objects.create(name=risk_data['name'], description=risk_data['description'])
        for field_data in risk_data['fields']:
            field = risk.fields.create(name=field_data['name'], description=field_data['description'])
            for choice in field_data['choices']:
                field.choices.create(choice=choice)

    def get(self, request, format=None):
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        try:
            self.__validate_data__(data)
            self.__persist_risk__(data)
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class RiskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer