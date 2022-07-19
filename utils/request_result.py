import allure
from deepdiff import DeepDiff
from jsonpath_ng import parse
from jsonschema import RefResolver, ValidationError
from openapi_core.contrib.requests import RequestsOpenAPIRequest, \
    RequestsOpenAPIResponse
from openapi_core.validation.response.validators import ResponseValidator
from openapi_schema_validator import validate
from requests import Response

from schema.jsonschema import Schema
from specification.specification import spec
from utils.attachment_manager import attach_json


class RequestResult:
    def __init__(self, response: Response):
        self.response = response

    def assert_status_code_is(self, status_code):
        with allure.step(f'Status code of response is {status_code}'):
            expected = status_code
            actual = self.response.status_code
            assert actual == expected, \
                f'Expected status code: {expected}, actual: {actual}'

    def assert_body_equal(self, body):
        with allure.step(f'Body of response equals'):
            attach_json('Expected', body)
            attach_json('Actual', self.response.json())
            diff = DeepDiff(self.response.json(), body)
            assert len(diff.items()) == 0, f'Not equals: {diff}'

    def assert_field_equal(self, field, value):
        with allure.step(f'Field "{field}" body of response equals "{value}"'):
            attach_json('Body', self.response.json())
            expected = str(value)
            actual = parse(field).find(self.response.json())[0].value
            assert actual == expected, \
                f'Expected value: {expected}, actual: {actual} '

    def validate_json_schema(self, json_schema: Schema):
        with allure.step(f'Validate json schema'):
            schema = json_schema.json_schema()
            attach_json('Schema', schema)
            ref_schema = json_schema.ref_schema()
            ref_resolver = RefResolver.from_schema(ref_schema)
            try:
                validate(self.response.json(), schema, resolver=ref_resolver)
            except ValidationError as exc:
                raise AssertionError(exc)

    def validate_specification_api(self):
        api = f'{self.response.request.method} {self.response.request.url}'
        with allure.step(f'Validate specification: {api}'):
            request = RequestsOpenAPIRequest(self.response.request)
            response = RequestsOpenAPIResponse(self.response)
            validator = ResponseValidator(spec)
            result = validator.validate(request, response)
            if len(result.errors) > 0:
                raise AssertionError(result.errors)
