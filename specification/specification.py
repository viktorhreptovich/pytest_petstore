from openapi_core import create_spec
from yaml import safe_load

with open('specification/swagger.yaml', 'r') as spec_file:
    spec_dict = safe_load(spec_file)

spec = create_spec(spec_dict)
