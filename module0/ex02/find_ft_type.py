
def all_thing_is_obj(object: any) -> int:
    if type(object) is list or \
        type(object) is dict or \
        type(object) is set or \
        type(object) is tuple:
        print(type(object))
    elif type(object) is str:
        print(f"{object} is in the kitchen {type(object)}")
    else:
        print("Type not found")
    return 42
