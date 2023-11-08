import sys
import json

waehrend_envs = {}


def do_funktion(envs, args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["funktion", params, body]


def do_aufrufen(envs, args):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs, arg) for arg in arguments]

    func = envs_get(envs, name)
    assert isinstance(func, list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params, values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs, body)
    envs.pop()

    return result


def envs_get(envs, name):
    assert isinstance(name, str)
    for e in reversed(envs):
        if name in e:
            return e[name]

    assert False, f"Unknown variable name {name}"


def envs_set(envs, name, value):
    assert isinstance(name, str)

    envs[-1][name] = value


def envs_delete(envs, name):
    assert isinstance(name, str)

    del envs[-1][name]


def do_setzen(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    var_name = args[0]
    value = do(envs, args[1])
    envs_set(envs, var_name, value)
    return value


def do_abrufen(envs, args):
    assert len(args) == 1
    return envs_get(envs, args[0])


def do_addieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left + right


def do_absolutwert(envs, args):
    assert len(args) == 1
    value = do(envs, args[0])
    return abs(value)


def do_subtrahieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left - right


def do_multiplizieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left * right


def do_dividieren(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left / right


def do_hochrechnen(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    return left ** right


def do_ausgeben(envs, args):
    assert len(args) > 0
    statements = []
    for arg in args:
        statements.append(do(envs, arg))

    print(' '.join(map(str, statements)))


def do_leq(env, args):
    assert len(args) == 2
    return do(env, args[0]) <= do(env, args[1])


def do_waehrend(envs, args):
    print(args)
    assert len(args) == 2
    while do(envs, args[0]):
        res = do(envs, args[1])
    return res


def do_liste(envs, args):
    assert len(args) == 3
    size = round(do(envs, args[0]))
    assert isinstance(size, int)
    assert isinstance(args[1], str)
    assert isinstance(args[2], list)

    assert len(
        args[2]) == size, f"Defined list size is {size}, but actual size is {len(args[2])}"

    new_list = []
    for item in args[2]:
        new_list.append(do(envs, item))

    list_name = args[1]
    value = new_list
    envs_set(envs, list_name, value)
    return value


def do_listen_wert_holen(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    assert isinstance(round(do(envs, args[1])), int)
    list_name = args[0]
    position = round(do(envs, args[1]))
    list_from_env = envs_get(envs, list_name)

    # Make sure the found element is actually a list
    assert isinstance(
        list_from_env, list), f"{list_name} is not a list, but a {type(list_from_env)}"
    return list_from_env[position]


def do_listen_wert_setzen(envs, args):
    assert len(args) == 3
    assert isinstance(args[0], str)
    assert isinstance(round(do(envs, args[1])), int)
    list_name = args[0]
    position = round(do(envs, args[1]))
    list_from_env = envs_get(envs, list_name)
    new_value = do(envs, args[2])

    # Make sure the found element is actually a list
    assert isinstance(
        list_from_env, list), f"{list_name} is not a list, but a {type(list_from_env)}"
    list_from_env[position] = new_value
    return list_from_env


def do_lexikon(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    assert isinstance(args[1], list)

    dict_name = args[0]
    values = args[1]
    new_dict = {}
    for items in values:
        new_dict[do(envs, items[0])] = do(envs, items[1])
    envs_set(envs, dict_name, new_dict)
    return new_dict


def do_lexikon_wert_holen(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    dict_name = args[0]
    key = args[1]
    dict_from_env = envs_get(envs, dict_name)

    # Make sure the found element is actually a dict
    assert isinstance(
        dict_from_env, dict), f"{dict_name} is not a dict, but a {type(dict_from_env)}"
    return dict_from_env[key]


def do_lexikon_wert_setzen(envs, args):
    assert len(args) == 3
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    dict_name = args[0]
    key = args[1]
    dict_from_env = envs_get(envs, dict_name)
    new_value = do(envs, args[2])

    # Make sure the found element is actually a dict
    assert isinstance(
        dict_from_env, dict), f"{dict_name} is not a dict, but a {type(dict_from_env)}"
    dict_from_env[key] = new_value
    return dict_from_env


def do_lexika_zusammenfuehren(envs, args):
    assert len(args) == 3
    for arg in args:
        assert isinstance(arg, str)
    new_dict_name = args[0]
    dict1_name = args[1]
    dict2_name = args[2]

    dict1 = envs_get(envs, dict1_name)
    dict2 = envs_get(envs, dict2_name)
    assert isinstance(
        dict1, dict), f"{dict1_name} is not a dict, but a {type(dict1)}"
    assert isinstance(
        dict2, dict), f"{dict2_name} is not a dict, but a {type(dict2)}"

    # Merge dictionaries to new dictionary
    new_dict = dict1 | dict2

    # save the new dictionary
    envs_set(envs, new_dict_name, new_dict)

    # delete the old dictionaries from the environement
    envs_delete(envs, dict1_name)
    envs_delete(envs, dict2_name)

    return new_dict

def do_klasse_definieren(envs, args):
    assert len(args) >= 2
    class_name = args[0]
    class_body = args[1:]

    # Create the class definition
    class_def = {
        "methods": {},
        "properties": [],
        "constructor": None,
        "base_class": None
    }

    # Process the class body to fill the class definition
    for item in class_body:
        if item[0] == "konstruktor":
            class_def["constructor"] = {
                "name": item[1],
                "params": item[2]
            }
        elif item[0] == "methode":
            method_name = item[1]
            class_def["methods"][method_name] = {
                "params": item[2],
                "body": item[3]
            }
        # Add more processing if needed for properties, inheritance, etc.

    # Save the class definition in the environment
    envs_set(envs, class_name, class_def)
    return class_def

def do_objekt_erstellen(envs, args):
    assert len(args) >= 2
    class_name = args[0]
    instance_properties = args[1:]

    # Retrieve the class definition from the environment
    class_def = envs_get(envs, class_name)
    assert isinstance(class_def, dict), f"{class_name} is not a class definition"
    assert class_def["constructor"] is not None, f"{class_name} does not have a constructor"

    # Create the object instance as a dictionary
    object_instance = {
        "class": class_name,
        "properties": dict(zip(class_def["constructor"]["params"], instance_properties))
    }

    # If there's a constructor, call it
    #if class_def["constructor"]:
    #    constructor_name = class_def["constructor"]["name"]
    #    do_methode_aufrufen(envs, [object_instance, constructor_name] + instance_properties)

    return object_instance

def do_vererbung(envs, args):
    assert len(args) == 3
    child_class_name, base_class_name, child_class_body = args
    base_class = envs_get(envs, base_class_name)
    assert isinstance(base_class, dict), f"{base_class_name} is not a class"
    child_class_definition = do_klasse_definieren(envs, [child_class_name] + child_class_body)
    
    # Inherit methods from the base class
    child_class_definition["methods"].update(base_class["methods"])
    
    child_class_definition["base_class"] = base_class
    return child_class_definition

def do_methode_aufrufen(envs, args):
    assert len(args) >= 2
    object_instance = args[0]
    method_name = args[1]
    method_args = args[2:]

    # Ensure the object instance is a dictionary
    assert isinstance(object_instance, dict), "First argument must be an object"

    # Retrieve the method from the class definition
    class_def = envs_get(envs, object_instance["class"])
    method = class_def["methods"][method_name]

    # Prepare the environment for the method 
    local_env = object_instance["properties"].copy()
    local_env.update(zip(method["params"], method_args))

    # Call the method
    return do(envs + [local_env], method["body"])


def do_abfolge(envs, args):
    assert len(args) > 0
    for operation in args:
        result = do(envs, operation)
    return result


OPERATIONS = {
    func_name.replace("do_", ""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


def do(envs, expr):
    if isinstance(expr, int) or isinstance(expr, float):
        return expr
    if isinstance(expr, str) and expr in waehrend_envs:
        expr = waehrend_envs[expr]
        return expr
    if isinstance(expr, str):
        return expr

    assert isinstance(expr, list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])


def main():
    assert len(sys.argv) == 2, "Usage: funcs-demo.py filename.gsc"
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    envs = [{}]
    result = do(envs, program)
    print(f"=> {result}")


if __name__ == "__main__":
    main()
