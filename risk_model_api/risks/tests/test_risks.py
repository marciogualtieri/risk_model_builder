from rest_framework import status
from rest_framework.test import APITestCase
from risks.tests.test_utils import TestUtils

class RiskViewSetTests(APITestCase, TestUtils):

    fixtures = ['fixtures/test_data.json']

    def test_get_all_risks(self):
        response = self.client.get('/risks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risks = self.__parse_response__(response)
        self.assertEqual(len(risks), 3)
        self.assertIsNotNone(risks)

    def test_get_a_risk_by_primary_key(self):
        response = self.client.get('/risks/%d/' % self.AUTOMOBILE_RISK_ID)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risk = self.__parse_response__(response)
        self.__validate_risk__(risk)

    def test_create_a_risk(self):
        response = self.client.post('/risks/', self.VALID_TEST_RISK, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_attempt_to_create_a_risk_missing_fields(self):
        response = self.client.post('/risks/', self.MISSING_FIELDS_TEST_RISK, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("'fields' is a required property" in self.__decode_content__(response))

    def test_attempt_to_create_a_risk_field_non_enum_with_choices(self):
        response = self.client.post('/risks/', self.NON_ENUM_WITH_CHOICES_TEST_RISK, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("is not valid under any of the given schemas" in self.__decode_content__(response))

    def test_attempt_to_create_a_risk_field_enum_with_less_than_two_choices(self):
        response = self.client.post('/risks/', self.ENUM_WITH_LESS_THAN_TWO_CHOICES_TEST_RISK, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("is not valid under any of the given schemas" in self.__decode_content__(response))