import sys
import json
import uuid
from datetime import datetime


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        if not kwargs.get("file", None):
            return original_function(*args, **kwargs)
        else:
            logging_file = kwargs.get("file", None)
            function_name = original_function.__name__
            unique_id = str(uuid.uuid4())
            start_time = datetime.now()
            logging_file.write(f"{unique_id}, {function_name}, start, {start_time}\n")
            result = original_function(*args, **kwargs)
            end_time = datetime.now()
            difference = end_time.microsecond - start_time.microsecond
            print(f"time = {difference}")
            logging_file.write(f"{unique_id}, {function_name}, stop, {end_time}\n")
            return result

    return wrapper_function


@decorator_function
def do_funktion(envs, args, file=None):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["funktion", params, body]


@decorator_function
def do_aufrufen(envs, args, file=None):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs, arg, file=file) for arg in arguments]

    func = envs_get(envs, name)
    assert isinstance(func, list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params, values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs, body, file=file)
    envs.pop()

    return result


@decorator_function
def envs_get(envs, name, file=None):
    assert isinstance(name, str)
    for e in reversed(envs):
        if name in e:
            return e[name]

    assert False, f"Unknown variable name {name}"


@decorator_function
def envs_set(envs, name, value, file=None):
    assert isinstance(name, str)

    envs[-1][name] = value


@decorator_function
def envs_delete(envs, name, file=None):
    assert isinstance(name, str)

    del envs[-1][name]


@decorator_function
def do_setzen(envs, args, file=None):
    assert len(args) == 2
    assert isinstance(args[0], str)
    var_name = args[0]
    value = do(envs, args[1], file=file)
    envs_set(envs, var_name, value)
    return value


@decorator_function
def do_abrufen(envs, args, file=None):
    assert len(args) == 1
    return envs_get(envs, args[0])


@decorator_function
def do_addieren(envs, args, file=None):
    assert len(args) == 2
    left = do(envs, args[0], file=file)
    right = do(envs, args[1], file=file)
    return left + right


@decorator_function
def do_absolutwert(envs, args, file=None):
    assert len(args) == 1
    value = do(envs, args[0], file=file)
    return abs(value)


@decorator_function
def do_subtrahieren(envs, args, file=None):
    assert len(args) == 2
    left = do(envs, args[0], file=file)
    right = do(envs, args[1], file=file)
    return left - right


@decorator_function
def do_multiplizieren(envs, args, file=None):
    assert len(args) == 2
    left = do(envs, args[0], file=file)
    right = do(envs, args[1], file=file)
    return left * right


@decorator_function
def do_dividieren(envs, args, file=None):
    assert len(args) == 2
    left = do(envs, args[0], file=file)
    right = do(envs, args[1], file=file)
    return left / right


@decorator_function
def do_hochrechnen(envs, args, file=None):
    assert len(args) == 2
    left = do(envs, args[0], file=file)
    right = do(envs, args[1], file=file)
    return left ** right


@decorator_function
def do_ausgeben(envs, args, file=None):
    assert len(args) > 0
    statements = []
    for arg in args:
        statements.append(do(envs, arg, file=file))

    print(' '.join(map(str, statements)))


@decorator_function
def do_kleinerAls(env, args, file=None):
    assert len(args) == 2
    return do(env, args[0], file=file) < do(env, args[1], file=file)


@decorator_function
def do_groesserAls(env, args, file=None):
    assert len(args) == 2
    return do(env, args[0], file=file) > do(env, args[1], file=file)


@decorator_function
def do_gleich(env, args, file=None):
    assert len(args) == 2
    return do(env, args[0], file=file) == do(env, args[1], file=file)


@decorator_function
def do_waehrend(envs, args, file=None):
    assert len(args) == 2
    while do(envs, args[0], file=file):
        res = do(envs, args[1], file=file)
    return res


@decorator_function
def do_liste(envs, args, file=None):
    assert len(args) == 3
    size = round(do(envs, args[0], file=file))
    assert isinstance(size, int)
    assert isinstance(args[1], str)
    assert isinstance(args[2], list)

    assert len(
        args[2]) == size, f"Defined list size is {size}, but actual size is {len(args[2])}"

    new_list = []
    for item in args[2]:
        new_list.append(do(envs, item, file=file))

    list_name = args[1]
    value = new_list
    envs_set(envs, list_name, value)
    return value


@decorator_function
def do_listen_wert_holen(envs, args, file=None):
    assert len(args) == 2
    assert isinstance(args[0], str)
    assert isinstance(round(do(envs, args[1], file=file)), int)
    list_name = args[0]
    position = round(do(envs, args[1], file=file))
    list_from_env = envs_get(envs, list_name)

    # Make sure the found element is actually a list
    assert isinstance(
        list_from_env, list), f"{list_name} is not a list, but a {type(list_from_env)}"
    return list_from_env[position]


@decorator_function
def do_listen_wert_setzen(envs, args, file=None):
    assert len(args) == 3
    assert isinstance(args[0], str)
    assert isinstance(round(do(envs, args[1])), int)
    list_name = args[0]
    position = round(do(envs, args[1], file=file))
    list_from_env = envs_get(envs, list_name)
    new_value = do(envs, args[2], file=file)

    # Make sure the found element is actually a list
    assert isinstance(
        list_from_env, list), f"{list_name} is not a list, but a {type(list_from_env)}"
    list_from_env[position] = new_value
    return list_from_env


@decorator_function
def do_lexikon(envs, args, file=None):
    assert len(args) == 2
    assert isinstance(args[0], str)
    assert isinstance(args[1], list)

    dict_name = args[0]
    values = args[1]
    new_dict = {}
    for items in values:
        new_dict[do(envs, items[0], file=file)] = do(envs, items[1], file=file)
    envs_set(envs, dict_name, new_dict)
    return new_dict


@decorator_function
def do_lexikon_wert_holen(envs, args, file=None):
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


@decorator_function
def do_lexikon_wert_setzen(envs, args, file=None):
    assert len(args) == 3
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    dict_name = args[0]
    key = args[1]
    dict_from_env = envs_get(envs, dict_name)
    new_value = do(envs, args[2], file=file)

    # Make sure the found element is actually a dict
    assert isinstance(
        dict_from_env, dict), f"{dict_name} is not a dict, but a {type(dict_from_env)}"
    dict_from_env[key] = new_value
    return dict_from_env


@decorator_function
def do_lexika_zusammenfuehren(envs, args, file=None):
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


@decorator_function
def do_machen(envs, args, file=None):
    assert len(args) >= 1
    cls = do(envs, args[0], file=file)
    additional_args = args[1:] if len(args) > 1 else []
    new_args = [cls["_new"]]
    new_args.extend(additional_args)
    res = do_aufrufen(envs, new_args, file=file)
    return res


def find(cls_name, method_name, envs):
    cls = envs_get(envs, cls_name)
    if cls == "None":
        raise NotImplementedError("method_name")
    if method_name in cls:
        return cls[method_name]
    return find(cls["_parent"], method_name, envs)


@decorator_function
def do_rufen(envs, args, file=None):
    assert len(args) >= 2
    cls_command = args[0]  # ["abrufen", "classname"]
    cls = do(envs, args[0], file=file)  # dict
    method_name = args[1]
    additional_args = args[2:] if len(args) > 2 else []
    method = find(cls["_class"], method_name, envs)  # returns name of method
    # formate to -> [method, ["abrufen", "classname"], additional_arg] (e.g. ["shape_density, ["abrufen", "sq"], 5]
    new_args = [method, cls_command]
    if additional_args:
        new_args.extend(additional_args)
    return do_aufrufen(envs, new_args, file=file)


@decorator_function
def do_abfolge(envs, args, file=None):
    assert len(args) > 0
    for operation in args:
        result = do(envs, operation, file=file)
    return result


OPERATIONS = {
    func_name.replace("do_", ""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


@decorator_function
def do(envs, expr, file=None):
    if isinstance(expr, int) or isinstance(expr, float):
        return expr
    if isinstance(expr, str):
        return expr

    assert isinstance(expr, list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:], file=file)


def main():
    assert len(sys.argv) >= 2, "Usage: funcs-demo.py filename.gsc"
    optional_file = None
    if len(sys.argv) > 2 and sys.argv[2] == "--trace":
        assert len(sys.argv) == 4, f"trace missing logging file {sys.argv}"
        optional_file = open(sys.argv[3], "w")
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    envs = [{}]
    result = do(envs, program, file=optional_file if optional_file else None)
    if optional_file:
        optional_file.close()
    print(f"=> {result}")


if __name__ == "__main__":
    main()
