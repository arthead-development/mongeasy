import re

def mongeasy_validate(schema, data):
    for field, rules in schema.items():
        if not isinstance(rules, dict):
            continue
        if rules.get('required') and field not in data:
            return f'{field} is required'

        value = data.get(field)

        if value is None:
            continue

        if rules['type'] == 'string' and not isinstance(value, str):
            return f'{field} must be a string'
        elif rules['type'] == 'integer' and not isinstance(value, int):
            return f'{field} must be an integer'
        elif rules['type'] == 'list' and not isinstance(value, list):
            return f'{field} must be a list'
        elif rules['type'] == 'dict' and not isinstance(value, dict):
            return f'{field} must be a dict'

        if rules.get('regex') and not re.match(rules['regex'], value):
            return f'{field} does not match the expected pattern'

        if rules.get('schema'):
            sub_schema = rules['schema']
            if rules['type'] == 'list':
                for item in value:
                    error = mongeasy_validate(sub_schema, item)
                    if error:
                        return error
            else:
                error = mongeasy_validate(sub_schema, value)
                if error:
                    return error

    return None