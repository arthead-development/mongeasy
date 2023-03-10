from mongeasy.exceptions import MongEasyValidationException
from pydantic.error_wrappers import ValidationError
from mongeasy.mongeasy_schema import mongeasy_validate 
from voluptuous import MultipleInvalid

def validate(schema_type, schema, data):
    if schema_type == 'mongeasy':
        mongeasy_schema = mongeasy_validate(schema, data)
        if mongeasy_schema is not None:
            raise MongEasyValidationException(f'There was errors validating the data using mongeasy schema:\n{mongeasy_schema}')
    elif schema_type == 'marshmallow':
        marshmallow_validator(schema, data)
    elif schema_type == 'voluptuous':
        voluptuous_validator(schema, data)
    elif schema_type == 'pydantic':
        pydantic_validator(schema, data)

def pydantic_validator(schema, data):
    try:
        model = schema(**data)
        #_ = model.dict()
    except ValidationError as e:
        model_name = schema.__name__
        error_msg = f'There was errors validating the data using pydantic schema {model_name}:\n'
        error_msg += '\n'.join([f'{loc}: {error["msg"]}' for error in e.errors() for loc in error['loc'] if loc != 'root'])
        
        raise MongEasyValidationException(error_msg)
    
def marshmallow_validator(schema, data):
    validation_schema = schema()
    errors = validation_schema.validate(data)
    if errors:
        error_msg = ''
        for error_field, error in errors.items():
            if isinstance(error, list):
                error_msg += f'{error_field}: {";".join([e for e in error])}\n'
            elif isinstance(error, dict):
                error_msg += f'{error_field}: \n'
                for k, v in error.items():
                    error_msg += f'\t{error_field}[{k}]'
                    for kk, vv in v.items():
                        for kkk, vvv in vv.items():
                            error_msg += f'[\'{kkk}\']: {"; ".join([issue for issue in vvv])}\n'
        #errors = '\n'.join([f"{field}: {error}" for field, field_errors in errors.items() for error in field_errors])
        raise MongEasyValidationException(f'There was errors validating the data using marshmallow schema {schema.__name__}:\n{error_msg}')
    
def voluptuous_validator(schema, data):
    try:
        schema(data)
    except MultipleInvalid as e:
        raise