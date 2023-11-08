Multiplication:
["multiplizieren", ["aufrufen", var1], ["aufrufen", var2]]
Division:
["dividieren", ["aufrufen", var1], ["aufrufen", var2]] //var2 uf 0 checke
Power:
["hochrechnen", ["aufrufen", nummer], ["aufrufen", exponent]]
Print:
["ausgeben", ..., ..., ...]
While:
["waehrend", while_condition(e.g. ["setzen", "var1", "test"]), while_statement(e.g. ["abfolge", ["ausgeben", ["abrufen","i"]], ["setzen", "i",["addieren", ["abrufen", "i"], 1]]])]
lists:
["liste", size, "list_name", list]
["listen_wert_holen", "list_name", index]
["listen_wert_setzen", "list_name", index, new_value]
Dictionary:
["lexikon", "dict_name", dictionary]
["lexikon_wert_holen", "dict_name", "keyname"]
["lexikon_wert_setzen", "dict_name", "keyname", new_value]
["lexika_zusammenfuehren", "new_dict_name", "dict1_name", "dict2_name"]