import sys
import json


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


def do_kleinerAls(env, args):
    assert len(args) == 2
    return do(env, args[0]) < do(env, args[1])


def do_groesserAls(env, args):
    assert len(args) == 2
    return do(env, args[0]) > do(env, args[1])


def do_gleich(env, args):
    assert len(args) == 2
    return do(env, args[0]) == do(env, args[1])


def do_waehrend(envs, args):
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


def do_machen(envs, args):
    assert len(args) >= 1
    cls = do(envs, args[0])
    additional_args = args[1:] if len(args) > 1 else []
    new_args = [cls["_new"]]
    new_args.extend(additional_args)
    res = do_aufrufen(envs, new_args)
    return res


def find(cls_name, method_name, envs):
    cls = envs_get(envs, cls_name)
    if cls == "None":
        raise NotImplementedError("method_name")
    if method_name in cls:
        return cls[method_name]
    return find(cls["_parent"], method_name, envs)


def do_rufen(envs, args):
    assert len(args) >= 2
    cls_command = args[0]  #["abrufen", "classname"]
    cls = do(envs, args[0])  # dict
    method_name = args[1]
    additional_args = args[2:] if len(args) > 2 else []
    method = find(cls["_class"], method_name, envs)  # returns name of method
    #formate to -> [method, ["abrufen", "classname"], additional_arg] (e.g. ["shape_density, ["abrufen", "sq"], 5]
    new_args = [method, cls_command]
    if additional_args:
        new_args.extend(additional_args)
    return do_aufrufen(envs, new_args)


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
