import python_jsonschema_objects as pjs
import json

schema = '''{
    "title": "Example Schema",
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        },
        "dogs": {
            "type": "array",
            "items": {"type": "string"},
            "maxItems": 4
        },
        "gender": {
            "type": "string",
            "enum": ["male", "female"]
        }
        },
    "required": ["firstName", "lastName"]
} '''

schema = json.loads(schema)
builder = pjs.ObjectBuilder(schema)
ns = builder.build_classes()
Person = ns.ExampleSchema
russel = Person(firstName="Russeel", lastName="Crow",age = 10, gender = 'male',dogs = ['Sugar','blue'])
print(russel.firstName)
print(russel.dogs[0])
