# Mongeasy

**Mongeasy** has been created to simplify the use of MongoDB in your projects. It is a simple and lightweight Python library that allows you to use MongoDB in a simple way.

```python
from mongeasy import create_document_class

# Create a document class, User, 
# using the MongoDB collection 'users' 
# and register it in the local namespace
create_document_class('User', 'users')

# Create a new user
user = User(name='John', age=30)
# Save it to the database
user.save()
```	

## Installation
Mongeasy is available on PyPi and can be installed using pip:
```bash
pip install mongeasy
```
It has been tested with Python 3.7+.

## Supported features
- Dynamically create document classes
- Create, update and delete documents
- Query documents
- Create indexes
- Automatic connection to MongoDB using configuration file or environment variables
- Support for schemas using [Pydantic](https://pydantic-docs.helpmanual.io/), [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) or [Voluptuous](http://alecthomas.github.io/voluptuous/docs/_build/html/index.html)
- Documents are handling data both as Python objects and as dictionaries
- Lists of documents or lists within documents are of a special type that allows you to work with them with ease

## Overall Goals
The main idea behind **Mongeasy** is to provide a simple and lightweight library that allows you to use MongoDB in a simple way. It is not intended to be a full-featured ORM, but rather a simple and lightweight library that makes every day access to a MongoDB hazzle free so you can focus on creating your application.

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

