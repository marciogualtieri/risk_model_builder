from risks.models import Risk, Field, Choice
from rest_framework.serializers import ModelSerializer, RelatedField
from collections import OrderedDict


EMPTY_VALUES = [None, [], '', {}]


class ChoiceListingField(RelatedField):
    def to_representation(self, value):
        return value.choice


class FieldSerializer(ModelSerializer):
    choices = ChoiceListingField(many=True, read_only=True)

    def __without_empty_values__(self, dictionary):
        return OrderedDict(
                   (name, value) \
                   for name, value in dictionary.items() \
                   if value not in EMPTY_VALUES
               )

    def to_representation(self, value):
        representation = super(ModelSerializer, self).to_representation(value)
        return self.__without_empty_values__(representation)

    class Meta:
        model = Field
        fields = ['id', 'name', 'description', 'type', 'choices']


class RiskSerializer(ModelSerializer):

    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ['id', 'name', 'description', 'fields']