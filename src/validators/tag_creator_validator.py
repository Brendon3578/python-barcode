from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def tag_creator_validator(request: any) -> None:
    '''
    Validate request body with a specific schema, using the Cerberus validator
    '''
    schema = {
        "product_code": {
            "type": "string",
            "required": True,
            "empty": False
        }
    }
    body_validator = Validator(schema)

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
