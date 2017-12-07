from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class RiskViewSetTests(APITestCase):

    AUTOMOBILE_RISK_ID = 67

    fixtures = ['fixtures/test_data.json']

    def __validate_enum_field__(self, enum_field):
        self.assertEqual(enum_field['id'], 75)
        self.assertEqual(enum_field['name'], 'Married')
        self.assertEqual(enum_field['description'], "The ol\' ball & chain.")
        self.assertEqual(enum_field['type'], 'enum')
        self.assertEqual(len(enum_field['choices']), 2)
        self.assertEqual(enum_field['choices'][0], 'Yes')
        self.assertEqual(enum_field['choices'][1], 'No')

    def __validate_text_field__(self, text_field):
        self.assertEqual(text_field['id'], 76)
        self.assertEqual(text_field['name'], 'Name')
        self.assertEqual(text_field['description'], 'Your full name.')
        self.assertEqual(text_field['type'], 'text')

    def __validate_fields__(self, fields):
        self.__validate_enum_field__(fields[0])
        self.__validate_text_field__(fields[1])

    def __validate_risk__(self, risk):
        self.assertEqual(risk['id'], self.AUTOMOBILE_RISK_ID)
        self.assertEqual(risk['name'], 'Automobile')
        self.assertEqual(risk['description'], 'An automobile insurance.')
        self.assertEqual(len(risk['fields']), 2)
        self.__validate_fields__(risk['fields'])

    def __parse_response__(self, response):
        return json.loads(response.content.decode('utf-8'))

    def test_get_all_risks(self):
        response = self.client.get('/risks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        page = self.__parse_response__(response)
        self.assertEqual(page['count'], 3)
        self.assertIsNotNone(page['results'])

    def test_get_a_specific_risk(self):
        response = self.client.get('/risks/%d/' % self.AUTOMOBILE_RISK_ID)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risk = self.__parse_response__(response)
        self.__validate_risk__(risk)
