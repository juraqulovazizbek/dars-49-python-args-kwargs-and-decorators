import json


def is_json(fn):
    def wrapper(name: str):
        if name.endswith('.json'):
            return fn(name)
        raise Exception('json file bolishi shart.')
    return wrapper

@is_json
def read_db(db_name: str) -> str:
    with open(db_name) as f:
        return json.load(f)

print(read_db('db.txt'))


# def decorate(fn):
#     def wrapper(name: str):
#         name = name.title()
#         fn(name)
#     return wrapper

# @decorate
# def fn(name):
#     print(f'nima gap: {name}')

# fn('ali valiyev')
