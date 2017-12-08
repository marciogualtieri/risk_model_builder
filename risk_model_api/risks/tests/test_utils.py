import json
from risks.models import Risk

class TestUtils:

    AUTOMOBILE_RISK_ID = 70

    VALID_TEST_RISK = {
                  'name': 'Test Risk',
                  'description': 'Test Risk Description',
                  'fields': [
                     { 'name': 'Test Field',
                       'description': 'Test Field Description',
                       'type': 'enum',
                       'choices': ['Test Choice 1', 'Test Choice 2', 'Test Choice 3']
                     }
                   ]
    }

    MISSING_FIELDS_TEST_RISK = {
                  'name': 'Test Risk',
                  'description': 'Test Risk Description'
    }

    NON_ENUM_WITH_CHOICES_TEST_RISK = {
                  'name': 'Test Risk',
                  'description': 'Test Risk Description',
                  'fields': [
                     { 'name': 'Test Field',
                       'description': 'Test Field Description',
                       'type': 'text',
                       'choices': ['Test Choice 1', 'Test Choice 2', 'Test Choice 3']
                     }
                   ]
    }

    ENUM_WITH_LESS_THAN_TWO_CHOICES_TEST_RISK = {
                  'name': 'Test Risk',
                  'description': 'Test Risk Description',
                  'fields': [
                     { 'name': 'Test Field',
                       'description': 'Test Field Description',
                       'type': 'enum',
                       'choices': ['Test Choice 1']
                     }
                   ]
    }

    def __decode_content__(self, response):
        return response.content.decode('utf-8')

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
        return json.loads(self.__decode_content__(response))