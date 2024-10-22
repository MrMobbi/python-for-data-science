
def isNan(value):
    return value != value

def print_object(object):
    loc = locals()
    for name, value in loc.items():
        print(f"{name}: {value} {type(object)}")

def NULL_not_found(object: any) -> int:
    if isNan(object):
        print_object(object)
        return 0
    elif object is None:
        print_object(object)
        return 0
    elif object == 0:
        print_object(object)
        return 0
    elif object == "":
        print_object(object)
        return 0
    elif object == False:
        print_object(object)
        return 0
    print("Type not found")
    return 1
