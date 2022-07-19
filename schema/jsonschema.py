from enum import Enum
from json import load

with open('schema/schema.json', 'r') as schema_file:
    schemas = load(schema_file)


class Schema(Enum):
    PET = 'Pet'
    ORDER = 'Order'
    USER = 'User'
    API_RESPONSE = 'ApiResponse'

    def json_schema(self):
        return schemas['definitions'][self.value]

    def ref_schema(self):
        return schemas
